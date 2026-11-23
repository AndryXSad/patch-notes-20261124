#!/usr/bin/env python3
"""Real-Life Patch Notes — make.fun bounty entry.

Writes one patch-note line (at most 160 characters) for a bug in
human biology to /output/entry.txt, where the house judge reads it.
Standard library only, deterministic, no network, no input files.
"""

import os
from pathlib import Path

# The entry: a terse release-note fix for the brain's 3 a.m. habit of
# replaying old embarrassments — a bug every human recognises, stated
# as if the fix just shipped. 123 characters.
LINE = (
    "v1.4.3: fixed a bug where the brain, at 3:00 a.m., replayed "
    "every embarrassing moment since 2009 in 4K with no skip button."
)


def main() -> None:
    # Gate check first: the sealed scorer wants UTF-8 text of 1 to 160
    # characters, not only white space. This line is 123 characters.
    if not 1 <= len(LINE) <= 160 or not LINE.strip():
        raise SystemExit("line fails the 1-160 character gate")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
