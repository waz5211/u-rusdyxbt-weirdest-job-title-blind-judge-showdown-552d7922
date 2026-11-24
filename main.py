#!/usr/bin/env python3
"""Write one weird job title to /output/entry.txt.

Deterministic, standard library only, no network, no randomness.
"""

import os

TITLE = "Director of Lost Socks, Left Foot Division"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TITLE + "\n")


if __name__ == "__main__":
    main()
