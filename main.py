#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes the one-line confession to /output/entry.txt.
Python 3.13, stdlib only, no network.
"""

import os

ENTRY = (
    "I ran DROP TABLE users on production instead of staging, "
    "then blamed the cache for an hour. "
    "The cache was innocent. I was not."
)


def main() -> None:
    # Gate: the entry must be a single line of 1-200 characters.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
