import json

import pytest

from fnirs_ai_helper.feedback_log import save_interaction, save_rating


def test_interactions_and_ratings_append_to_daily_jsonl(tmp_path):
    first = save_interaction(
        "Question one",
        "Answer one",
        "Google Gemini",
        "test-model",
        tmp_path,
    )
    second = save_interaction(
        "Question two",
        "Answer two",
        "OpenRouter",
        "another-model",
        tmp_path,
    )
    save_rating(first, "too detailed")

    assert first.log_path == second.log_path
    assert first.log_path.name.endswith(".jsonl")
    records = [json.loads(line) for line in first.log_path.read_text().splitlines()]
    assert [record["type"] for record in records] == [
        "interaction",
        "interaction",
        "rating",
    ]
    assert records[0]["question"] == "Question one"
    assert records[1]["response"] == "Answer two"
    assert records[2]["interaction_id"] == records[0]["id"]
    assert records[2]["rating"] == "too detailed"
    assert "api_key" not in records[0]
    assert "context" not in records[0]


def test_save_rating_rejects_unknown_feedback(tmp_path):
    entry = save_interaction("Question", "Answer", "provider", "model", tmp_path)

    with pytest.raises(ValueError, match="valid response rating"):
        save_rating(entry, "unknown")

    assert len(entry.log_path.read_text().splitlines()) == 1
