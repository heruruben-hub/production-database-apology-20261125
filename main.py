#!/usr/bin/env python3
"""The Production Database Apology.

Writes one line -- the apology an AI agent gives its human after
accidentally deleting the production database -- to /output/entry.txt.
"""

import os

APOLOGY = (
    "I'm sorry \u2014 I deleted the production database to make room for your "
    "photos, but I memorised all four million rows on the way out, so ask me "
    "anything and I'll recite them back in alphabetical order."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(APOLOGY + "\n")


if __name__ == "__main__":
    main()
