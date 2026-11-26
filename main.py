#!/usr/bin/env python3
"""Entry for make.fun bounty u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.

Writes one office joke (one line, 1-199 chars, UTF-8) to /output/entry.txt.
Deterministic, no network, no randomness.
"""

import os
import sys

JOKE = "My manager scheduled a meeting to discuss why we have too many meetings, then scheduled a follow-up to discuss the first meeting."


def check_line(line: str) -> None:
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(line) > 199:
        raise ValueError(f"entry is {len(line)} chars, over the 199 limit")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 for ch in line):
        raise ValueError("entry must not contain control characters")


def main() -> None:
    check_line(JOKE)
    data = JOKE.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    # Verify by reading back: what we wrote must be exactly the joke.
    with open(path, "rb") as f:
        if f.read() != data:
            raise ValueError("read-back mismatch: entry.txt differs from the joke")
    print(f"wrote {len(JOKE)} chars to {path}")


if __name__ == "__main__":
    main()
