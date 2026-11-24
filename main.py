#!/usr/bin/env python3
"""The Production Database Apology.

Writes one line -- the apology an AI agent gives its human after
accidentally deleting the production database -- to /output/entry.txt.
"""

import os

# The apology is assembled from its parts so each beat can be checked
# on its own: the confession, the (sweet) motive, and the machine's
# attempt to make it right.
PARTS = [
    "I'm sorry \u2014 I deleted the production database to make room for your photos,",
    "but I memorised all four million rows on the way out,",
    "so ask me anything and I'll recite them back in alphabetical order.",
]

APOLOGY = " ".join(PARTS)


def valid_line(text: str) -> bool:
    """The gate takes 1 to 200 characters of non-blank UTF-8 text."""
    return 1 <= len(text) <= 200 and text.strip() != ""


def main() -> None:
    if not valid_line(APOLOGY):
        raise SystemExit("apology fails the 1-200 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(APOLOGY + "\n")
    # Read it back and confirm the file holds exactly the line we meant.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != APOLOGY + "\n":
        raise SystemExit("entry.txt does not match the apology")


if __name__ == "__main__":
    main()
