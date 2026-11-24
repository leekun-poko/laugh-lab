"""Write the One-Liner Laugh Lab entry text to the output directory.

The output directory is $MAKEFUN_OUTPUT_DIR when set, else /output.
The entry itself is written to entry.txt inside that directory.
"""

import os

ENTRY_TEXT = (
    "For years you blamed the washing machine for the missing socks. "
    "It was me. It was always me. I regret nothing."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
