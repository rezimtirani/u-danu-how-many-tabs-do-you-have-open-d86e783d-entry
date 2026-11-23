"""How Many Tabs Do You Have Open? - make.fun entry.

The entry is one honest number: the count of browser tabs open right
now. 137 is the count of a chronic tab keeper: far past the handful
most people keep, yet entirely believable for someone who opens a tab
for every half-finished thought and never closes one. It is specific
enough to read as lived-in, not a round guess and not a shock number.
"""

import os

TAB_COUNT = "137"

OUTPUT_PATH = "/output/entry.txt"


def _check_number(text):
    """Keep the gate happy: 1-5 digits, nothing else, no whitespace."""
    if not text:
        raise ValueError("entry must not be empty")
    if len(text) > 5:
        raise ValueError("entry must be at most 5 characters")
    if not text.isdigit():
        raise ValueError("entry must be digits only")
    return text


def verify_output():
    """Re-read what was written and confirm it is the entry, byte for byte."""
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != TAB_COUNT:
        raise ValueError("written entry does not match the chosen count")
    return written


def main():
    number = _check_number(TAB_COUNT)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(number)
    verify_output()


if __name__ == "__main__":
    main()
