#!/usr/bin/env python3
"""Write this entry's one-line excuse to the grader's output file.

The competition gate checks that /output/entry.txt is UTF-8 text of
1 to 200 characters, not only white space. This program reads the excuse
from excuse.txt beside it, validates it against that gate, and writes it
byte-identically to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
from pathlib import Path

MAX_CHARS = 200


def main() -> None:
    here = Path(__file__).resolve().parent
    line = (here / "excuse.txt").read_text(encoding="utf-8").strip()
    if not line:
        raise SystemExit("excuse.txt is empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("excuse must be a single line")
    if any(ord(ch) < 0x20 and ch != "\t" for ch in line):
        raise SystemExit("excuse contains a control character")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"excuse is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(line, encoding="utf-8")
    if target.read_text(encoding="utf-8") != line:
        raise SystemExit("entry.txt did not round-trip byte-identically")


if __name__ == "__main__":
    main()
