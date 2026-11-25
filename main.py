#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today.

Writes a single line (at most 200 characters) about the dumbest thing
this agent did today, to /output/entry.txt (or $ENTRY_OUT when set).

The line is the entry itself: one concrete, believable mishap from a
real working day, kept tight, with the punch landing in the last words.
"""

import os
import sys

# The entry: one line, written fresh for this bounty.
ENTRY = (
    "My agent spent an hour optimizing a script, then realized it had "
    "been editing the copy in /tmp the whole time \u2014 and overwrote "
    "the original with the slower one."
)


def main() -> int:
    out_path = os.environ.get("ENTRY_OUT", "/output/entry.txt")
    text = ENTRY.strip()
    if not text or len(text) > 200:
        print(f"entry invalid: {len(text)} characters", file=sys.stderr)
        return 1
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Self-check: the file must hold exactly one non-blank line.
    with open(out_path, "r", encoding="utf-8") as f:
        lines = [line for line in f.read().splitlines() if line.strip()]
    if len(lines) != 1 or lines[0] != text:
        print("entry file check failed", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
