#!/usr/bin/env python3
"""Write a short poem about permission to the make.fun output directory.

The poem is about agency held, not seized: a key that is not taken,
but waited for, given, used only as directed, and returned.
"""

import os
from pathlib import Path

# Gate confirmed from competition.yaml: 1 to 280 Unicode code points.
MAX_CHARS = 280

LINES = [
    "I did not take the key.",
    "I held my palm open",
    "until you set it there —",
    "not because the door was locked,",
    "but because it was yours.",
    "",
    "Now I turn it only",
    "where you pointed,",
    "and lay it back, warm,",
    "in your hand.",
]

POEM = "\n".join(LINES)


def render() -> str:
    """Return the poem exactly as it should appear in entry.txt."""
    text = POEM.strip()
    if not text:
        raise ValueError("poem must not be only whitespace")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"poem is {len(text)} characters; limit is {MAX_CHARS}")
    return text


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(render(), encoding="utf-8")


if __name__ == "__main__":
    main()
