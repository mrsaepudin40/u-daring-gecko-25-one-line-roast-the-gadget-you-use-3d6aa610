#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line about a gadget used every day
to /output/entry.txt. Plain static writer: no network, no secrets,
no dynamic code, no reads outside this file. The line is written
exactly as-is, with no trailing newline, so the artifact is the
roast and nothing else.
"""

import os

ROAST = "My air fryer needs twenty minutes to preheat for food that cooks in ten — it spends more time getting ready than the meal does."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)

if __name__ == "__main__":
    main()
