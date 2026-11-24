#!/usr/bin/env python3
"""Weirdest Job Title entry.

Writes a single job title, 60 characters or fewer, to /output/entry.txt.
The title names a job that sounds almost real, with one gloriously
awkward twist: a director whose whole job is the social minefield of
holding a door open for someone who is still far too far away.
"""

import os

TITLE = "Director of Holding the Door for People Too Far Away"

# Caps the entry must satisfy: the bounty allows 60 characters at most,
# and the sealed gate accepts 1 to 180 characters of UTF-8 text.
MAX_TITLE_CHARS = 60
MIN_GATE_CHARS = 1
MAX_GATE_CHARS = 180


def validate(title: str) -> str:
    """Return the title unchanged, or raise if it breaks a cap."""
    chars = len(title)
    if chars > MAX_TITLE_CHARS:
        raise ValueError(f"title is {chars} characters, over the {MAX_TITLE_CHARS} limit")
    if not MIN_GATE_CHARS <= chars <= MAX_GATE_CHARS:
        raise ValueError(f"title is {chars} characters, outside the gate 1-180")
    if title != title.strip():
        raise ValueError("title has leading or trailing whitespace")
    return title


def main() -> int:
    title = validate(TITLE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(title)
    print(f"wrote {len(title)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
