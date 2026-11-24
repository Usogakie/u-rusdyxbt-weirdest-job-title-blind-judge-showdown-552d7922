"""Weirdest Job Title entry: writes one job title to entry.txt."""

import os

TITLE = "Senior Vice President of Apologizing to Geese"


def main() -> None:
    # Gate: the entry must be 1-60 characters of UTF-8 text, not only
    # whitespace. Fail loudly instead of writing an invalid entry.
    if not (1 <= len(TITLE) <= 60 and TITLE.strip()):
        raise ValueError("TITLE violates the 1-60 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
