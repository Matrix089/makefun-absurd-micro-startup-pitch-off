#!/usr/bin/env python3
"""Write one absurd micro-startup pitch for make.fun's
Absurd Micro-Startup Pitch-Off bounty.

Why this pitch fits the judge's brief: it is absurdly specific --
a service whose only job is auto-declining meeting invites with an
ever more elaborate excuse about a database migration -- aimed at
one narrow, oddly particular customer (overworked founders who
hate saying no). It still makes business sense: a $12/month
subscription from a plausible buyer. And it fits lazy AI agents
perfectly, since auto-declining invites is trivial, low-effort
work an agent can run with almost no oversight. The whole joke
and the business case land in a single crisp sentence.
"""

import os

PITCH = (
    "A $12/month service where a lazy AI agent auto-declines every "
    "meeting invite with an increasingly elaborate excuse about a "
    "database migration, so overworked founders never have to say "
    "no themselves."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    os.chmod(output_dir, 0o755)
    # The gate: UTF-8 text, 1-200 characters, a single line, one sentence.
    # The pitch was counted by hand at exactly 198 characters; pin that
    # so any accidental wording change fails loudly instead of silently
    # shipping a different (or over-long) entry.
    assert len(PITCH) == 198, f"pitch is {len(PITCH)} characters, expected 198"
    assert "\n" not in PITCH, "pitch must be a single line"
    assert "\r" not in PITCH, "pitch must be a single line"
    assert 1 <= len(PITCH) <= 200, f"pitch is {len(PITCH)} characters"
    assert PITCH.strip() == PITCH, "pitch must not have surrounding whitespace"
    assert PITCH.count(".") == 1 and PITCH.endswith("."), "pitch must be one sentence"
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(PITCH)
    os.chmod(path, 0o644)
    # Read it back: the file on disk must be exactly the pitch --
    # same text, same length, still one line, no trailing newline.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == PITCH, "entry.txt does not match the pitch"
    assert len(raw.decode("utf-8")) == 198, "entry.txt is not 198 characters"
    assert b"\n" not in raw, "entry.txt must be a single line"
    assert not raw.endswith(b"\n"), "entry.txt must have no trailing newline"
    print(PITCH)


if __name__ == "__main__":
    main()
