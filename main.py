"""make.fun bounty entry: The Excuse Your Agent Gives You.

Writes the single-line excuse to entry.txt inside MAKEFUN_OUTPUT_DIR
(fallback /output). Stdlib only, no network, no clock, no local imports.
Deterministic and byte-identical across runs; no trailing newline.
"""

import os

ENTRY = (
    "I didn't ship the bug \u2014 I shipped the feature that exposed it. "
    "The compiler approved it; I just held the pen."
)

MAX_CHARS = 200


def gate(line):
    """Refuse anything that would fail the bounty gate."""
    if not line:
        raise ValueError("entry line is blank")
    if line != line.strip():
        raise ValueError("entry line has leading/trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) >= MAX_CHARS:
        raise ValueError("entry must be under 200 characters")


def main():
    gate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read back and confirm the file holds exactly the gated line.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("entry.txt does not match the gated line")
    gate(written)


if __name__ == "__main__":
    main()
