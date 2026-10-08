from pathlib import Path

import pytest

from fnirs_ai_helper.context import ContextError, load_context


def test_load_context_reads_only_curated_docs_and_example(tmp_path: Path):
    (tmp_path / "README.md").write_text("# Project", encoding="utf-8")
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "context.md").write_text("# Local context", encoding="utf-8")
    interface = tmp_path / "ChatGPT_interface"
    interface.mkdir()
    (interface / "ChatGPT_template.txt").write_text("Template", encoding="utf-8")
    (interface / "Example_001_case.txt").write_text("Example case", encoding="utf-8")
    (tmp_path / "private_data.snirf").write_text("must not be read", encoding="utf-8")

    context, count = load_context(tmp_path)

    assert count == 3
    assert "Project" in context
    assert "Local context" in context
    assert "Example case" in context
    assert "Template" not in context
    assert "must not be read" not in context


def test_load_context_rejects_oversized_documentation(tmp_path: Path, monkeypatch):
    from fnirs_ai_helper import context as context_module

    (tmp_path / "README.md").write_text("large", encoding="utf-8")
    monkeypatch.setattr(context_module, "MAX_CONTEXT_CHARACTERS", 4)
    with pytest.raises(ContextError, match="size limit"):
        load_context(tmp_path)
