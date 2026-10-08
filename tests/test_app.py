import os
import time
import json

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import pytest
from PySide6.QtCore import QEventLoop, QTimer
from PySide6.QtWidgets import QApplication, QLineEdit, QTextBrowser

from fnirs_ai_helper.app import AssistantWindow, EXAMPLE_QUESTION


@pytest.fixture(scope="module")
def qt_app():
    app = QApplication.instance() or QApplication([])
    yield app


class FakeCredentialStore:
    def __init__(self):
        self.keys = {"gemini": "gemini-test-key", "openrouter": "openrouter-test-key"}

    def get_api_key(self, provider="gemini"):
        return self.keys.get(provider)

    def save_api_key(self, api_key, provider="gemini"):
        self.keys[provider] = api_key

    def delete_api_key(self, provider="gemini"):
        self.keys.pop(provider, None)


def test_window_can_select_openrouter_with_separate_key_and_model(qt_app):
    credentials = FakeCredentialStore()
    credentials.save_api_key("router-key", "openrouter")
    window = AssistantWindow(credential_store=credentials)
    try:
        assert window._provider.currentText() == "OpenRouter"
        assert window._model.currentText() == "openrouter/free"
        window._provider.setCurrentText("OpenRouter")

        assert window._model.currentText() == "openrouter/free"
        assert window._key_status.text() == (
            "OpenRouter key saved in OS credential store."
        )
        assert window._settings_button.text() == "OpenRouter API key…"
        assert window._ask_button.text() == "Ask OpenRouter"
        window._model.setCurrentText("custom/provider-model")
        window._provider.setCurrentText("Google Gemini")
        window._provider.setCurrentText("OpenRouter")
        assert window._model.currentText() == "custom/provider-model"
    finally:
        window.close()


def test_window_starts_with_example_prompt_and_read_only_answer(qt_app):
    window = AssistantWindow(credential_store=FakeCredentialStore())
    try:
        assert window._question.toPlainText() == EXAMPLE_QUESTION
        assert isinstance(window._answer, QTextBrowser)
        assert window._answer.isReadOnly()
        assert not window._answer.openLinks()
        assert not window._answer.openExternalLinks()
        assert window._progress.text() == "Ready."
        assert window._model.currentText() == "openrouter/free"
    finally:
        window.close()


def test_answer_renders_markdown_and_saves_feedback(qt_app, tmp_path):
    window = AssistantWindow(
        credential_store=FakeCredentialStore(),
        development_log_dir=tmp_path,
    )
    try:
        window._request_details = ("test question", "Google Gemini", "test-model")
        window._show_answer(
            "## Use the Stimulus Manager\n\n"
            "Choose **Onset to Offset marks**.\n\n"
            "- Select the start marker\n"
            "- Select the end marker"
        )

        rendered_html = window._answer.document().toHtml()
        assert "font-size:x-large" in rendered_html
        assert "font-weight:700" in rendered_html
        assert "<ul" in rendered_html
        assert "Choose Onset to Offset marks." in window._answer.toPlainText()
        assert window._feedback_rating.count() == 6
        assert not window._save_feedback_button.isEnabled()
        assert len(list(tmp_path.glob("*.jsonl"))) == 1

        window._feedback_rating.setCurrentText("Ok response")
        assert window._save_feedback_button.isEnabled()
        window._save_feedback_button.click()

        log_path = next(tmp_path.glob("*.jsonl"))
        records = [json.loads(line) for line in log_path.read_text().splitlines()]
        assert [record["type"] for record in records] == ["interaction", "rating"]
        assert records[0]["response"].startswith("## Use the Stimulus Manager")
        assert records[1]["rating"] == "Ok response"
        assert records[1]["interaction_id"] == records[0]["id"]
    finally:
        window.close()


def test_api_key_input_is_masked(qt_app):
    from fnirs_ai_helper.app import _ApiKeyDialog

    dialog = _ApiKeyDialog(FakeCredentialStore(), "Google Gemini")
    try:
        key_input = dialog.findChild(QLineEdit)
        assert key_input is not None
        assert key_input.echoMode() == QLineEdit.Password
    finally:
        dialog.close()


def test_request_error_is_displayed_and_ask_button_is_reenabled(
    qt_app, monkeypatch
):
    import fnirs_ai_helper.app as app_module

    class FailingProvider:
        _api_key = "openrouter-test-key"

        def __init__(self, **kwargs):
            pass

        def answer(self, question, context):
            time.sleep(0.05)
            raise TimeoutError("Gemini did not return within 60 seconds.")

    monkeypatch.setattr(app_module, "OpenRouterProvider", FailingProvider)
    monkeypatch.setattr(app_module, "load_context", lambda: ("context", 1))
    window = AssistantWindow(credential_store=FakeCredentialStore())
    loop = QEventLoop()
    try:
        window._ask()
        assert window._thread is not None
        window._thread.finished.connect(loop.quit)
        QTimer.singleShot(2_000, loop.quit)
        loop.exec()

        assert "TimeoutError" in window._answer.toPlainText()
        assert "within 60 seconds" in window._answer.toPlainText()
        assert "request failed" in window._progress.text().lower()
        assert window._ask_button.isEnabled()
    finally:
        window.close()


def test_submitted_question_is_copied_cleared_and_followed_by_answer(
    qt_app, monkeypatch, tmp_path
):
    import fnirs_ai_helper.app as app_module

    class AnsweringProvider:
        _api_key = "openrouter-test-key"

        def __init__(self, **kwargs):
            pass

        def answer(self, question, context):
            time.sleep(0.05)
            return (
                "Use **Onset to Offset marks** from the Stimulus Manager. "
                "Would you like to confirm the odd/even convention?"
            )

    monkeypatch.setattr(app_module, "OpenRouterProvider", AnsweringProvider)
    monkeypatch.setattr(app_module, "load_context", lambda: ("context", 1))
    window = AssistantWindow(
        credential_store=FakeCredentialStore(),
        development_log_dir=tmp_path,
    )
    loop = QEventLoop()
    try:
        question = "How do I set event durations?"
        window._question.setPlainText(question)
        window._ask()

        assert window._question.toPlainText() == ""
        assert question in window._answer.toPlainText()

        assert window._thread is not None
        window._thread.finished.connect(loop.quit)
        QTimer.singleShot(2_000, loop.quit)
        loop.exec()

        transcript = window._answer.toPlainText()
        assert transcript.index(question) < transcript.index("Onset to Offset marks")
        assert transcript.index("Would you like") > transcript.index("Onset to Offset marks")
        html = window._answer.document().toHtml()
        assert "#174ea6" in html
        assert "#c00000" in html
        assert "font-weight:700" in html
        user_question = window._answer.document().find(question)
        assert user_question.charFormat().foreground().color().name() == "#174ea6"
        assistant_question = window._answer.document().find("Would you like")
        assert assistant_question.charFormat().foreground().color().name() == "#c00000"
        answer_text = window._answer.document().find("Use")
        assert answer_text.charFormat().foreground().color().name() != "#c00000"
        records = [
            json.loads(line)
            for path in tmp_path.glob("*.jsonl")
            for line in path.read_text().splitlines()
        ]
        assert records[0]["question"] == question
        assert records[0]["response"].startswith("Use **Onset")
    finally:
        window.close()
