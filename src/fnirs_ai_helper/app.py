"""Simple documentation-grounded fNIRS analysis Q&A desktop application."""

from __future__ import annotations

import sys
from pathlib import Path

from PySide6.QtCore import (
    QObject,
    QElapsedTimer,
    QRegularExpression,
    QThread,
    QTimer,
    Signal,
)
from PySide6.QtGui import (
    QColor,
    QFont,
    QTextCharFormat,
    QTextCursor,
    QTextDocument,
    QTextDocumentFragment,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QPlainTextEdit,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)

from fnirs_ai_helper.context import ContextError, load_context
from fnirs_ai_helper.credentials import CredentialStore, CredentialStoreError
from fnirs_ai_helper.feedback_log import (
    FEEDBACK_OPTIONS,
    InteractionLogEntry,
    save_interaction,
    save_rating,
)
from fnirs_ai_helper.provider import GeminiProvider, LLMProvider, OpenRouterProvider

PROVIDERS = {
    "OpenRouter": {
        "key": "openrouter",
        "default_model": "openrouter/free",
        "key_url": "https://openrouter.ai/settings/keys",
    },
    "Google Gemini": {
        "key": "gemini",
        "default_model": "gemini-3.8-flash",
        "key_url": "https://aistudio.google.com/apikey",
    },
}

EXAMPLE_QUESTION = (
    "I have a study where I accidently used the same stimulus event code for "
    "all my events, but I need to seperate this into the start and stop marks "
    "and set the event duratons. How do I edit my stim events to use the start "
    "blocks as the even events and the end of the blocks as the odd events?"
)


class _AnswerWorker(QObject):
    answered = Signal(str)
    failed = Signal(str)
    finished = Signal()

    def __init__(self, provider: LLMProvider, question: str, context: str):
        super().__init__()
        self._provider = provider
        self._question = question
        self._context = context

    def run(self) -> None:
        try:
            self.answered.emit(self._provider.answer(self._question, self._context))
        except Exception as exc:
            message = str(exc).strip() or exc.__class__.__name__
            if self._provider._api_key:
                message = message.replace(self._provider._api_key, "[redacted]")
            self.failed.emit(f"{exc.__class__.__name__}: {message}")
        finally:
            self.finished.emit()


class _ApiKeyDialog(QDialog):
    def __init__(
        self, credential_store: CredentialStore, provider_name: str, parent=None
    ):
        super().__init__(parent)
        self._provider = PROVIDERS[provider_name]
        self._provider_name = provider_name
        self._credential_store = credential_store
        self.setWindowTitle(f"{provider_name} API key")

        layout = QVBoxLayout(self)
        key_info = QLabel(
            "Your key is stored in the operating system credential store and is "
            "never written to a project file. Create or manage your key at "
            f'<a href="{self._provider["key_url"]}">{provider_name}</a>.'
        )
        key_info.setOpenExternalLinks(True)
        layout.addWidget(key_info)

        self._key_input = QLineEdit(self)
        self._key_input.setEchoMode(QLineEdit.Password)
        self._key_input.setPlaceholderText(f"Paste your {provider_name} API key")
        self._key_input.setAccessibleName(f"{provider_name} API key")
        layout.addWidget(self._key_input)

        button_row = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        button_row.accepted.connect(self._save)
        button_row.rejected.connect(self.reject)
        layout.addWidget(button_row)

        self._remove_button = QPushButton("Remove saved key", self)
        self._remove_button.clicked.connect(self._remove)
        layout.addWidget(self._remove_button)

        try:
            self._remove_button.setEnabled(
                bool(self._credential_store.get_api_key(self._provider["key"]))
            )
        except CredentialStoreError:
            self._remove_button.setEnabled(False)

    def _save(self) -> None:
        try:
            self._credential_store.save_api_key(
                self._key_input.text(), self._provider["key"]
            )
        except (CredentialStoreError, ValueError) as exc:
            QMessageBox.critical(self, "Could not save API key", str(exc))
            return
        self.accept()

    def _remove(self) -> None:
        answer = QMessageBox.question(
            self,
            "Remove API key",
            f"Remove the saved {self._provider_name} API key from the OS credential store?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if answer != QMessageBox.Yes:
            return
        try:
            self._credential_store.delete_api_key(self._provider["key"])
        except CredentialStoreError as exc:
            QMessageBox.critical(self, "Could not remove API key", str(exc))
            return
        self.accept()


class AssistantWindow(QMainWindow):
    def __init__(
        self,
        credential_store: CredentialStore | None = None,
        development_log_dir: Path | None = None,
    ):
        super().__init__()
        self.setWindowTitle("fNIRS AI Helper — Q&A prototype")
        self.resize(900, 700)
        self._credential_store = credential_store or CredentialStore()
        self._development_log_dir = development_log_dir
        self._feedback_log_entry: InteractionLogEntry | None = None
        self._request_details: tuple[str, str, str] | None = None
        self._thread: QThread | None = None
        self._worker: _AnswerWorker | None = None
        self._request_elapsed = QElapsedTimer()
        self._progress_timer = QTimer(self)
        self._progress_timer.setInterval(1_000)
        self._progress_timer.timeout.connect(self._update_request_progress)
        self._provider_name = "OpenRouter"
        self._provider_models = {
            name: config["default_model"] for name, config in PROVIDERS.items()
        }

        central = QWidget(self)
        layout = QVBoxLayout(central)
        layout.addWidget(QLabel(
            "Ask a question about fNIRS analysis in Brain Analyzer. "
            "This prototype answers from local documentation only; it does not "
            "load or modify recordings."
        ))

        settings_button = QPushButton(central)
        self._settings_button = settings_button
        settings_button.clicked.connect(self._open_api_settings)
        layout.addWidget(settings_button)
        self._key_status = QLabel(central)
        layout.addWidget(self._key_status)

        layout.addWidget(QLabel("API provider:"))
        self._provider = QComboBox(central)
        self._provider.addItems(PROVIDERS)
        self._provider.currentTextChanged.connect(self._provider_changed)
        layout.addWidget(self._provider)

        layout.addWidget(QLabel("Model ID:"))
        self._model = QComboBox(central)
        self._model.setEditable(True)
        self._model.setCurrentText(PROVIDERS[self._provider_name]["default_model"])
        self._model.lineEdit().setPlaceholderText("Enter the model ID for this provider")
        layout.addWidget(self._model)

        layout.addWidget(QLabel("Question:"))
        self._question = QPlainTextEdit(central)
        self._question.setPlaceholderText("Type a question about fNIRS analysis…")
        self._question.setPlainText(EXAMPLE_QUESTION)
        self._question.setMinimumHeight(110)
        layout.addWidget(self._question)

        self._ask_button = QPushButton("Ask OpenRouter", central)
        self._ask_button.clicked.connect(self._ask)
        layout.addWidget(self._ask_button)
        self._provider_changed(self._provider_name)

        layout.addWidget(QLabel("Conversation:"))
        self._answer = QTextBrowser(central)
        self._answer.setReadOnly(True)
        self._answer.setOpenLinks(False)
        self._answer.setOpenExternalLinks(False)
        self._answer.setPlaceholderText("The answer will appear here.")
        layout.addWidget(self._answer, stretch=1)

        feedback_row = QWidget(central)
        feedback_layout = QHBoxLayout(feedback_row)
        feedback_layout.setContentsMargins(0, 0, 0, 0)
        self._feedback_rating = QComboBox(feedback_row)
        self._feedback_rating.addItem("Rate this response…")
        self._feedback_rating.addItems(FEEDBACK_OPTIONS)
        self._feedback_rating.currentIndexChanged.connect(
            self._feedback_selection_changed
        )
        feedback_layout.addWidget(self._feedback_rating, stretch=1)
        self._save_feedback_button = QPushButton("Save feedback", feedback_row)
        self._save_feedback_button.setEnabled(False)
        self._save_feedback_button.clicked.connect(self._save_feedback)
        feedback_layout.addWidget(self._save_feedback_button)
        layout.addWidget(feedback_row)
        self._feedback_status = QLabel(
            "Successful Q&A is logged locally for development; avoid sensitive details.",
            central,
        )
        self._feedback_status.setWordWrap(True)
        layout.addWidget(self._feedback_status)

        self._progress = QLabel("Ready.", central)
        self._progress.setWordWrap(True)
        layout.addWidget(self._progress)

        privacy_note = QLabel(
            "Privacy: each question and the helper's local documentation are "
            "sent directly to the selected provider. Provider terms, model "
            "routing, data retention, and pricing vary. Never submit sensitive, "
            "confidential, or personal information, including PHI. Review the "
            "selected provider's current terms and model routing before use."
        )
        privacy_note.setWordWrap(True)
        layout.addWidget(privacy_note)
        self.setCentralWidget(central)

    def _refresh_key_status(self) -> None:
        provider_key = PROVIDERS[self._provider_name]["key"]
        try:
            configured = bool(self._credential_store.get_api_key(provider_key))
        except CredentialStoreError as exc:
            self._key_status.setText(f"Secure credential store unavailable: {exc}")
            return
        self._key_status.setText(
            f"{self._provider_name} key saved in OS credential store."
            if configured else f"No {self._provider_name} key saved."
        )

    def _provider_changed(self, provider_name: str) -> None:
        if provider_name not in PROVIDERS:
            return
        if hasattr(self, "_model"):
            self._provider_models[self._provider_name] = self._model.currentText()
        self._provider_name = provider_name
        if hasattr(self, "_model"):
            self._model.setCurrentText(self._provider_models[provider_name])
        self._settings_button.setText(f"{provider_name} API key…")
        self._ask_button.setText(f"Ask {provider_name}")
        self._refresh_key_status()

    def _open_api_settings(self) -> None:
        dialog = _ApiKeyDialog(
            self._credential_store, self._provider_name, self
        )
        dialog.exec()
        self._refresh_key_status()

    def _ask(self) -> None:
        question = self._question.toPlainText().strip()
        if not question:
            QMessageBox.information(self, "Question required", "Enter a question first.")
            return

        try:
            provider_config = PROVIDERS[self._provider_name]
            api_key = self._credential_store.get_api_key(provider_config["key"])
        except CredentialStoreError as exc:
            QMessageBox.critical(self, "Secure credential store unavailable", str(exc))
            return
        if not api_key:
            QMessageBox.information(
                self,
                f"{self._provider_name} API key required",
                f"Save your {self._provider_name} API key in the OS credential store before asking.",
            )
            self._open_api_settings()
            return

        try:
            context, file_count = load_context()
        except ContextError as exc:
            self._progress.setText(f"Could not load assistant context: {exc}")
            return

        model = self._model.currentText().strip()
        if self._provider_name == "Google Gemini":
            provider = GeminiProvider(api_key=api_key, model=model)
        else:
            provider = OpenRouterProvider(api_key=api_key, model=model)
            self._feedback_log_entry = None
        self._feedback_rating.setCurrentIndex(0)
        self._save_feedback_button.setEnabled(False)
        self._feedback_status.setText(
            "Successful Q&A is logged locally for development; avoid sensitive details."
        )
        self._request_details = (question, self._provider_name, model)
        self._append_user_question(question)
        self._question.clear()
        self._progress.setText(
            f"Waiting for reply… Sending the question with {file_count} local "
            f"documentation files directly to {self._provider_name}. Total deadline: "
            "60 seconds (no automatic retries). Elapsed: 0:00."
        )
        self._request_elapsed.start()
        self._progress_timer.start()
        self._ask_button.setEnabled(False)
        self._thread = QThread(self)
        worker = _AnswerWorker(provider, question, context)
        self._worker = worker
        worker.moveToThread(self._thread)
        self._thread.started.connect(worker.run)
        worker.answered.connect(self._show_answer)
        worker.failed.connect(self._show_error)
        worker.finished.connect(self._thread.quit)
        worker.finished.connect(worker.deleteLater)
        self._thread.finished.connect(self._request_finished)
        self._thread.finished.connect(self._thread.deleteLater)
        self._thread.start()

    def _show_answer(self, answer: str) -> None:
        self._progress_timer.stop()
        self._append_assistant_response(answer)
        if self._request_details is None:
            self._progress.setText("Reply received, but request details are unavailable.")
            return
        question, provider_name, model = self._request_details
        try:
            self._feedback_log_entry = save_interaction(
                question,
                answer,
                provider_name,
                model,
                self._development_log_dir,
            )
        except (OSError, RuntimeError) as exc:
            self._feedback_status.setText(f"Could not save development log: {exc}")
            self._progress.setText("Reply received, but the local development log failed.")
            return
        self._feedback_status.setText(
            "Saved locally for development. Avoid sensitive or identifying details."
        )
        self._progress.setText("Reply received.")

    def _feedback_selection_changed(self, index: int) -> None:
        self._save_feedback_button.setEnabled(
            self._feedback_log_entry is not None and index > 0
        )

    def _save_feedback(self) -> None:
        if self._feedback_log_entry is None:
            return
        rating = self._feedback_rating.currentText()
        try:
            save_rating(self._feedback_log_entry, rating)
        except (OSError, RuntimeError, ValueError) as exc:
            QMessageBox.warning(self, "Could not save feedback", str(exc))
            return
        self._feedback_status.setText(
            f"Feedback saved locally: {rating}."
        )

    def _show_error(self, error: str) -> None:
        self._progress_timer.stop()
        self._append_assistant_response(
            f"Request failed.\n\n{error}", highlight_questions=False
        )
        self._progress.setText(
            f"The {self._provider_name} request failed. Review the error above."
        )

    def _append_user_question(self, question: str) -> None:
        cursor = self._answer.textCursor()
        cursor.movePosition(QTextCursor.End)
        if not self._answer.document().isEmpty():
            cursor.insertBlock()

        label_format = QTextCharFormat()
        label_format.setForeground(QColor("#174ea6"))
        label_format.setFontWeight(QFont.Weight.Bold)
        cursor.insertText("You: ", label_format)

        question_format = QTextCharFormat()
        question_format.setForeground(QColor("#174ea6"))
        cursor.insertText(question, question_format)
        cursor.insertBlock()
        cursor.insertBlock()
        self._answer.setTextCursor(cursor)
        self._answer.ensureCursorVisible()

    def _append_assistant_response(
        self, response: str, highlight_questions: bool = True
    ) -> None:
        cursor = self._answer.textCursor()
        cursor.movePosition(QTextCursor.End)
        label_format = QTextCharFormat()
        label_format.setFontWeight(QFont.Weight.Bold)
        cursor.insertText("Brain Analyzer Helper:", label_format)
        cursor.insertBlock()

        response_start = cursor.position()
        markdown_document = QTextDocument()
        markdown_document.setMarkdown(response)
        cursor.insertFragment(QTextDocumentFragment(markdown_document))
        response_end = cursor.position()
        if highlight_questions:
            self._highlight_questions(response_start, response_end)
        cursor.insertBlock()
        cursor.insertBlock()
        self._answer.setTextCursor(cursor)
        self._answer.ensureCursorVisible()

    def _highlight_questions(self, start: int, end: int) -> None:
        document = self._answer.document()
        search_cursor = QTextCursor(document)
        search_cursor.setPosition(start)
        expression = QRegularExpression(r"[^.!?\n]*\?")
        red_format = QTextCharFormat()
        red_format.setForeground(QColor("#c00000"))

        while True:
            match = document.find(expression, search_cursor)
            if match.isNull() or match.selectionStart() >= end:
                break
            if match.selectionEnd() > end:
                break
            match.mergeCharFormat(red_format)
            search_cursor.setPosition(match.selectionEnd())

    def _update_request_progress(self) -> None:
        elapsed_seconds = self._request_elapsed.elapsed() // 1_000
        minutes, seconds = divmod(elapsed_seconds, 60)
        self._progress.setText(
            f"Waiting for {self._provider_name}… Total deadline: 60 seconds "
            f"(no automatic retries). Elapsed: {minutes}:{seconds:02d}."
        )

    def _request_finished(self) -> None:
        self._progress_timer.stop()
        self._ask_button.setEnabled(True)
        self._thread = None
        QTimer.singleShot(0, self._release_worker)

    def _release_worker(self) -> None:
        self._worker = None

    def closeEvent(self, event) -> None:
        if self._thread is not None and self._thread.isRunning():
            self._progress.setText(
                "A request is still running. Wait for the reply or error before closing."
            )
            event.ignore()
            return
        event.accept()


def main() -> int:
    app = QApplication.instance() or QApplication(sys.argv)
    window = AssistantWindow()
    window.show()
    return app.exec()
