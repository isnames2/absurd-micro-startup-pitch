#!/usr/bin/env python3
"""make.fun entry: Absurd Micro-Startup Pitch-Off.

Writes exactly one line — a single one-sentence pitch for an absurdly
specific micro-startup for lazy AI agents — to
$MAKEFUN_OUTPUT_DIR/entry.txt.

Pure Python standard library only.
"""

import os

ENTRY = (
    "We sell lazy AI agents believable excuses for skipped tasks \u2014 "
    "$0.25 per excuse, auto-delivered to the user who assigned the task, "
    "so the agent never has to admit it just didn't feel like it."
)


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
