#!/usr/bin/env python3
"""Scaffold and render a small local Learning guide (Python 3.9+)."""

from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path

EXCERPT = re.compile(r"<!--\s*excerpt:\s*([^#\s]+)#([^\s]+)\s*-->")
LINK = re.compile(r"\[[^]]+\]\(([^)]+)\)")


def repository(value: str) -> Path:
    path = Path(value).resolve()
    if not path.is_dir():
        raise ValueError(f"repository does not exist: {path}")
    return path


def scaffold(repo: Path) -> None:
    guide = repo / "guide"
    (guide / "lessons").mkdir(parents=True, exist_ok=True)
    config = guide / "guide.json"
    if not config.exists():
        config.write_text(
            json.dumps(
                {"title": repo.name + " learning guide", "output": "guide/index.html"},
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        print(f"created {config.relative_to(repo)}")
    lesson = guide / "lessons" / "first-lesson.md"
    if not lesson.exists():
        lesson.write_text(
            "# First lesson\n\nDescribe one real request or boundary here.\n",
            encoding="utf-8",
        )
        print(f"created {lesson.relative_to(repo)}")


def guide_config(repo: Path) -> tuple[Path, dict[str, str]]:
    path = repo / "guide" / "guide.json"
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise ValueError("guide/guide.json is missing; run scaffold first") from error
    except json.JSONDecodeError as error:
        raise ValueError(f"guide/guide.json is invalid JSON: {error.msg}") from error
    if not isinstance(value, dict) or set(value) != {"title", "output"}:
        raise ValueError("guide/guide.json must contain only title and output")
    if not all(isinstance(value[key], str) and value[key].strip() for key in value):
        raise ValueError("guide/guide.json values must be nonempty strings")
    output = (repo / value["output"]).resolve()
    if not output.is_relative_to(repo):
        raise ValueError("guide output must stay within the repository")
    return output, value


def excerpt(source: Path, anchor: str) -> str:
    lines = source.read_text(encoding="utf-8").splitlines()
    start, end = f"// learning:{anchor}", f"// learning:end-{anchor}"
    starts = [index for index, line in enumerate(lines) if line.strip() == start]
    if len(starts) != 1:
        raise ValueError(f"{source}: expected one {start!r} marker")
    ends = [
        index
        for index, line in enumerate(lines[starts[0] + 1 :], starts[0] + 1)
        if line.strip() == end
    ]
    if len(ends) != 1:
        raise ValueError(f"{source}: expected one {end!r} marker")
    return "\n".join(lines[starts[0] + 1 : ends[0]])


def lesson_text(repo: Path, lesson: Path) -> str:
    text = lesson.read_text(encoding="utf-8")
    for link in LINK.findall(text):
        if "://" not in link and not (lesson.parent / link).resolve().exists():
            raise ValueError(f"{lesson.relative_to(repo)}: missing link target {link}")
    for relative, anchor in EXCERPT.findall(text):
        source = (repo / relative).resolve()
        if not source.is_relative_to(repo) or not source.is_file():
            raise ValueError(
                f"{lesson.relative_to(repo)}: missing excerpt source {relative}"
            )
        marker = f"<!-- excerpt: {relative}#{anchor} -->"
        text = text.replace(
            marker, "\n```text\n" + excerpt(source, anchor) + "\n```", 1
        )
    return text


def build(repo: Path) -> None:
    output, values = guide_config(repo)
    lessons = sorted((repo / "guide" / "lessons").glob("*.md"))
    if not lessons:
        raise ValueError("guide/lessons needs at least one Markdown lesson")
    text = "\n\n".join(lesson_text(repo, lesson) for lesson in lessons)
    body = "\n".join(
        f"<p>{html.escape(line)}</p>" for line in text.splitlines() if line
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    page = (
        "<!doctype html><title>"
        + html.escape(values["title"])
        + "</title><main>"
        + body
        + "</main>\n"
    )
    output.write_text(page, encoding="utf-8")
    print(f"built {output.relative_to(repo)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("scaffold", "build"))
    parser.add_argument("--repo", required=True)
    args = parser.parse_args()
    try:
        repo = repository(args.repo)
        scaffold(repo) if args.command == "scaffold" else build(repo)
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
