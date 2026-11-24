#!/usr/bin/env python3
"""Write one weird job title to /output/entry.txt.

Deterministic, standard library only, no network, no randomness.
"""

import os
import sys

TITLE = "Director of Lost Socks, Left Foot Division"


def main():
    if not TITLE.strip() or not 1 <= len(TITLE) <= 60:
        print(
            f"error: job title must be 1-60 non-blank characters, "
            f"got {len(TITLE)} characters",
            file=sys.stderr,
        )
        sys.exit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TITLE + "\n")


if __name__ == "__main__":
    main()
