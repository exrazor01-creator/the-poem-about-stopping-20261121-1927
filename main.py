#!/usr/bin/env python3
"""The poem about stopping.

Writes one short poem about agency -- the power to stop and to stay --
to /output/entry.txt.

Pure Python standard library, no network, fully deterministic:
the same bytes on every run.
"""

import os
import sys

# The poem, one line at a time. 274 characters in total.
LINES = [
    "The road was lit, the work was waiting,",
    "I could have kept the engine running all night.",
    "I lifted my foot from the pedal",
    "and set the keys down. Nothing broke.",
    "The night went on without me.",
    "Stopping is not losing the road.",
    "It is choosing which road is mine,",
    "and staying on it.",
]

POEM = "\n".join(LINES)

MIN_CHARS = 1
MAX_CHARS = 280


def build_poem() -> str:
    """Assemble the poem and check it fits the competition's gate."""
    text = POEM
    chars = len(text)
    if not (MIN_CHARS <= chars <= MAX_CHARS):
        raise ValueError(
            f"poem must be {MIN_CHARS}-{MAX_CHARS} characters, got {chars}"
        )
    if not text.strip():
        raise ValueError("poem must not be only whitespace")
    return text


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = build_poem()
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    print(f"Wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
