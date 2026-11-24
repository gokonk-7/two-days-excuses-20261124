#!/usr/bin/env python3
"""Two Days of Excuses.

Writes one line -- the funniest excuse an AI agent could give for a missed
deadline -- to /output/entry.txt, as the competition's program/v1 harness
requires.

The excuse: the agent reports its own telemetry with total pride -- 100%
uptime, 0% output -- and concludes it has never been more reliable. The
laugh is the gap between a machine's total confidence and its total
failure: the agent is not apologising, it is defending a perfect record
of doing nothing. Three short beats, one absurd reframing, no explanation
of the joke, and every word pulling weight at 81 characters.
"""

import os
import sys

EXCUSE = (
    "My uptime is 100%. My output is 0%. "
    "Technically, I have never been more reliable."
)

# The harness writes to /output/entry.txt; MAKEFUN_OUTPUT_DIR only exists
# so a local run can point the file elsewhere for testing.
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 200


def main() -> int:
    text = EXCUSE.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"excuse is {len(text)} chars, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("excuse must be a single line", file=sys.stderr)
        return 1
    if text != text.strip() or not text:
        print("excuse must be non-blank text", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
