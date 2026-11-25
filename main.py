"""Roast Your Fridge: one line, one laugh.

The entry is a single roast aimed at the most passive-aggressive
appliance in the kitchen: the fridge. It keeps the milk cold, holds
the leftovers hostage, and then has the nerve to sound its door alarm
as if its own owner were breaking in.

The program is deliberately deterministic: the same line is written
on every run, so both grading runs produce identical output.
"""

import os

LINE = (
    "My fridge keeps the milk cold and the leftovers hostage \u2014 "
    "open the door and it beeps like I broke into my own kitchen."
)

MAX_CHARS = 200


def validate(line):
    """Enforce every gate the brief puts on the entry text.

    Gates, in order: non-empty string, no leading or trailing
    whitespace, at most 200 characters, exactly one line, no control
    characters, not only whitespace, names the roast target, and no
    double spaces (a line that reads cleanly aloud has none).
    """
    if not isinstance(line, str):
        raise TypeError("entry must be a string")
    if not line:
        raise ValueError("entry must not be empty")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in line):
        raise ValueError("entry must not contain control characters")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "fridge" not in line.lower():
        raise ValueError("entry must roast the fridge by name")
    if "  " in line:
        raise ValueError("entry must not contain double spaces")
    return line


def main():
    line = validate(LINE)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(line + "\n")
    print(line)


if __name__ == "__main__":
    main()
