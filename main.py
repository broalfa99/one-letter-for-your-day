#!/usr/bin/env python3
"""One Letter for Your Day — make.fun entry.

Writes exactly one letter to /output/entry.txt: "Z" — zonked, zero sleep.
The gate requires UTF-8 text of exactly 1 character, not only
whitespace, so the program writes a single byte and nothing else.
The letter Z is the sleep symbol itself ("Zzz"), so it fits its word
better than any other letter fits its word: vivid, funny, and true.
"""

import os

LETTER = "Z"


def main() -> None:
    if len(LETTER) != 1 or not LETTER.isalpha():
        raise SystemExit("entry must be exactly one letter")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Round-trip check: what the grader reads must be exactly this letter.
    back = open("/output/entry.txt", encoding="utf-8").read()
    if back != LETTER:
        raise SystemExit(f"round-trip mismatch: {back!r}")
    print(f"wrote {LETTER!r} to /output/entry.txt")


if __name__ == "__main__":
    main()
