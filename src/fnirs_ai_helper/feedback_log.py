"""Append-only daily development log for assistant questions and feedback."""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from uuid import uuid4

FEEDBACK_OPTIONS = (
    "Ok response",
    "too detailed",
    "not detailed enough",
    "incorrect answer",
    "needs followup",
)
DEFAULT_LOG_DIRECTORY = Path(__file__).resolve().parents[2] / "development_logs"


@dataclass(frozen=True)
class InteractionLogEntry:
    interaction_id: str
    log_path: Path


def save_interaction(
    question: str,
    response: str,
    provider: str,
    model: str,
    log_directory: Path | None = None,
) -> InteractionLogEntry:
    """Append one successful Q&A to its local daily log."""
    now = datetime.now().astimezone()
    interaction_id = uuid4().hex
    record = {
        "type": "interaction",
        "id": interaction_id,
        "timestamp": now.isoformat(timespec="seconds"),
        "provider": provider,
        "model": model,
        "question": question,
        "response": response,
    }
    directory = log_directory or DEFAULT_LOG_DIRECTORY
    log_path = directory / f"{now.date().isoformat()}.jsonl"
    _append_record(log_path, record)
    return InteractionLogEntry(interaction_id, log_path)


def save_rating(entry: InteractionLogEntry, rating: str) -> None:
    """Append a rating event for a previously logged interaction."""
    if rating not in FEEDBACK_OPTIONS:
        raise ValueError("Choose a valid response rating.")
    record = {
        "type": "rating",
        "interaction_id": entry.interaction_id,
        "timestamp": datetime.now().astimezone().isoformat(timespec="seconds"),
        "rating": rating,
    }
    _append_record(entry.log_path, record)


def _append_record(log_path: Path, record: dict[str, str]) -> None:
    try:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        serialized = (json.dumps(record, ensure_ascii=False) + "\n").encode("utf-8")
        descriptor = os.open(
            log_path,
            os.O_WRONLY | os.O_APPEND | os.O_CREAT,
            0o600,
        )
        try:
            remaining = memoryview(serialized)
            while remaining:
                written = os.write(descriptor, remaining)
                if written == 0:
                    raise OSError("No log data was written.")
                remaining = remaining[written:]
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
    except OSError as exc:
        raise RuntimeError(f"Could not append to the development log: {exc}") from exc
