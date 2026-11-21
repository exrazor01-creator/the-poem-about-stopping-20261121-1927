"""Write "The poem about stopping" to entry.txt.

The program holds the poem as a list of lines, joins them with
newlines, validates the result, and writes it to the output
directory (``/output`` by default, overridable with the
``MAKEFUN_OUTPUT_DIR`` environment variable).
"""

import os
import sys


POEM_LINES = [
    "The road was lit, the work was waiting,",
    "I could have kept the engine running all night.",
    "I lifted my foot from the pedal",
    "and set the keys down. Nothing broke.",
    "The night went on without me.",
    "Stopping is not losing the road.",
    "It is choosing which road is mine,",
    "and staying on it.",
]

MIN_LENGTH = 1
MAX_LENGTH = 280
EXPECTED_LINES = 8


def build_poem(lines):
    """Join the poem lines into a single text block."""
    return "\n".join(lines)


def check_poem(text):
    """Make sure the poem is a real, non-empty text of valid length.

    Besides the 1-280 character window, the poem must have exactly
    eight lines — one per thought of the stopping driver — so a
    truncated or duplicated copy is caught before it is written.
    """
    if not text.strip():
        raise ValueError("poem is empty or only whitespace")
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise ValueError(
            f"poem must be {MIN_LENGTH}-{MAX_LENGTH} characters, "
            f"got {len(text)}"
        )
    line_count = len(text.splitlines())
    if line_count != EXPECTED_LINES:
        raise ValueError(
            f"poem must have {EXPECTED_LINES} lines, got {line_count}"
        )


def output_path():
    """Resolve the output file path from the environment or default."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(directory, "entry.txt")


def main():
    poem = build_poem(POEM_LINES)
    check_poem(poem)

    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(poem)

    print(f"Wrote {len(poem)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
