#!/usr/bin/env python3
"""Write one original line about a useless superpower to /output/entry.txt."""

import os

LINE = (
    "I can teleport anywhere on Earth, but only three inches "
    "to the left, and only on Tuesdays."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
