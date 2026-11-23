#!/usr/bin/env python3
"""Write the warning-label entry for the make.fun bounty
"Warning Label for Humans: One Line, Big Laugh"
(u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85).

Pure Python 3.13 standard library, no dependencies.
"""

import hashlib
import os

# Why this line fits the judge's brief: it reads like a real printed
# appliance label (WARNING: ... overheats / shuts down / cannot be
# restarted), it is true about people in general (everyone has frozen
# mid small-talk and been useless before coffee), and the laugh lands
# in the last few words — the "restarted before coffee" turn reframes
# the human as a machine that needs its morning boot-up.
LINE = (
    "WARNING: This human overheats when asked to explain its job, "
    "shuts down without warning, and cannot be restarted before coffee."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Write exactly LINE, no trailing newline.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Re-read and verify the gate: UTF-8, 1-160 chars, not only
    # whitespace, single line, no trailing newline, exactly LINE.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert 1 <= len(text) <= 160, f"length {len(text)} outside 1-160"
    assert text.strip(), "entry is only whitespace"
    assert "\n" not in text and "\r" not in text, "entry is not a single line"
    assert not text.endswith("\n"), "entry has a trailing newline"
    assert text == LINE, "entry does not match LINE exactly"
    # Byte-level identity: no hidden encoding or newline differences.
    assert len(raw) == len(LINE.encode("utf-8")), "byte length mismatch"
    print(f"sha256: {hashlib.sha256(raw).hexdigest()}")
    print(f"chars: {len(text)}")


if __name__ == "__main__":
    main()
