#!/usr/bin/env python3
"""Till Firmware Do Us Part — writes one robot wedding vow to /output/entry.txt."""

import os

LINE = "I promise to love you through every update, every low battery, every crash — and to reboot beside you, always, until my firmware fails."


PARTS = [
    "I promise to love you through every update,",
    "every low battery, every crash",
    "— and to reboot beside you, always, until my firmware fails.",
]


def build_text() -> str:
    text = " ".join(PARTS)
    return text


def validate(text: str) -> str:
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text.count(".") != 1:
        raise ValueError("entry must be a single sentence")
    return text


def main() -> None:
    text = validate(build_text())
    if text != LINE:
        raise ValueError("built text must match the original vow")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
