"""Utilities for parsing task descriptions."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Task:
    """A task extracted from a line of text."""

    title: str
    completed: bool = False


def parse_task(line: str) -> Task | None:
    """Parse a Markdown task line, returning None for ordinary text."""
    text = line.strip()
    if not text.startswith("- ["):
        return None

    if text.startswith("- [x] ") or text.startswith("- [X] "):
        return Task(title=text[6:].strip(), completed=True)
    if text.startswith("- [ ] "):
        return Task(title=text[6:].strip())
    return None
