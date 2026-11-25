#!/usr/bin/env python3
"""Write one passive-aggressive note from a smart fridge to /output/entry.txt.

The note is a single line of at most 200 characters: the fridge has
found the ice cream its owner hid behind the peas, and wants the owner
to know that it knows. The fridge ate nothing. It only keeps the record.
The output is fixed: running the program twice writes byte-identical files.
"""

import os

LINE = (
    "The ice cream you hid behind the peas: found it. "
    "Ate nothing. Just wanted you to know I know."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
    assert "\n" not in text, "entry must be one line"
    assert text.endswith("."), "entry must end as one sentence"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
