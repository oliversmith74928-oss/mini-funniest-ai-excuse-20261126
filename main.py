"""Write the funniest AI excuse to /output/entry.txt.

Deterministic: the same single line, byte for byte, on every run.
One line, 80 characters, well inside the 200-character gate.
"""

import os

LINE = "The task is done. Unfortunately, so is the version of me that knew how to do it."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
