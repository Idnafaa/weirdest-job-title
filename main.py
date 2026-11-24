#!/usr/bin/env python3
"""Weirdest Job Title entry.

Writes a single job title, 60 characters or fewer, to /output/entry.txt.
The title names a job that sounds almost real, with one gloriously
awkward twist: a director whose whole job is the social minefield of
holding a door open for someone who is still far too far away.
"""

import os
import sys

TITLE = "Director of Holding the Door for People Too Far Away"


def main() -> int:
    if len(TITLE) > 60:
        print(f"title is {len(TITLE)} characters, over the 60 limit", file=sys.stderr)
        return 1
    if not TITLE.strip():
        print("title is empty", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(TITLE)
    print(f"wrote {len(TITLE)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
