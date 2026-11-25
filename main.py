#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line joke about office life to
/output/entry.txt. Stdlib only, deterministic.

The line is assembled from parts so the setup and the punchline stay
separate in the source, and the finished line is validated against the
competition gate (UTF-8, 1-200 characters, not only whitespace) before
it is written.
"""

import os

# Setup: the boss summons the worker back to the office.
_SETUP = "My boss asked me to come into the office"
# Punchline: the reason inverts the point of working from home.
_PUNCHLINE = "so he could watch me work from home."

JOKE = _SETUP + " " + _PUNCHLINE


def _validate(text):
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    return encoded


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    data = _validate(JOKE)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
