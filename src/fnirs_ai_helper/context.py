"""Load the small, reviewed documentation set sent with each question."""

from pathlib import Path


class ContextError(RuntimeError):
    """Raised when the local assistant context cannot be assembled safely."""


MAX_CONTEXT_CHARACTERS = 50_000


def _context_paths(project_root: Path) -> list[Path]:
    paths = [project_root / "README.md"]
    paths.extend(sorted((project_root / "docs").rglob("*.md")))
    paths.extend(sorted(
        path
        for path in (project_root / "ChatGPT_interface").glob("Example_*.txt")
        if path.is_file()
    ))
    return [path for path in paths if path.is_file()]


def load_context(project_root: Path | None = None) -> tuple[str, int]:
    """Return repository documentation and its file count; never read data files."""
    root = project_root or Path(__file__).resolve().parents[2]
    sections = []
    for path in _context_paths(root):
        try:
            content = path.read_text(encoding="utf-8").strip()
        except (OSError, UnicodeError) as exc:
            raise ContextError(f"Could not read context file {path.name}: {exc}") from exc
        if content:
            relative_path = path.relative_to(root).as_posix()
            sections.append(f"## Context file: {relative_path}\n\n{content}")

    if not sections:
        raise ContextError("No assistant context documents were found.")

    context = "\n\n---\n\n".join(sections)
    if len(context) > MAX_CONTEXT_CHARACTERS:
        raise ContextError(
            "The selected documentation context exceeds the prototype size limit "
            f"of {MAX_CONTEXT_CHARACTERS:,} characters."
        )
    return context, len(sections)
