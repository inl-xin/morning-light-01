#!/usr/bin/env python3
"""Two Lines of Morning Light — make.fun bounty entry.

Writes a two-line micro poem (at most 120 characters including the
line break) to /output/entry.txt: the kettle clicks off, light
slides beneath the door — a letter the house has held its breath
all night to read.

Deterministic: the text is a constant, so every run writes the same
bytes. No network.
"""
import os

TEXT = (
    "The kettle clicks off; light slides beneath the door—\n"
    "a letter the house has held its breath all night to read."
)


def main():
    assert 1 <= len(TEXT) <= 120, f"text is {len(TEXT)} characters"
    assert TEXT.count("\n") == 1, "exactly two lines"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    print(f"wrote {path} ({len(TEXT)} characters)")


if __name__ == "__main__":
    main()
