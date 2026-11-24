"""Office joke entry for make.fun's "Make the AI Judge Laugh: the Office Joke Open".

Writes exactly one office joke - a single line, 90-170 characters, no trailing
newline - to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Pure Python standard library only; deterministic.
"""

import os

JOKE = (
    "My boss said to think outside the box, so I moved my desk into the "
    "hallway; now I have the only window office in the building and three "
    "HR complaints."
)

MIN_LEN = 90
MAX_LEN = 170


def validate(text):
    """Check the entry text meets the competition rules."""
    assert isinstance(text, str), "entry must be a string"
    assert "\n" not in text, "entry must be a single line"
    assert "\r" not in text, "entry must not contain carriage returns"
    assert not text.endswith("\n"), "entry must have no trailing newline"
    assert text == text.strip(), "entry must not have leading/trailing spaces"
    assert "  " not in text, "entry must not contain double spaces"
    assert all(32 <= ord(ch) <= 126 for ch in text), (
        "entry must contain only printable ASCII characters"
    )
    assert MIN_LEN <= len(text) <= MAX_LEN, (
        "entry must be %d-%d characters, got %d" % (MIN_LEN, MAX_LEN, len(text))
    )
    return True


def main():
    validate(JOKE)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    with open(path, "wb") as f:
        f.write(JOKE.encode("utf-8"))

    # Read the bytes back and re-validate what actually landed on disk.
    with open(path, "rb") as f:
        raw = f.read()
    assert not raw.endswith(b"\n"), "entry.txt must have no trailing newline"
    written = raw.decode("utf-8")
    assert written == JOKE, "entry.txt content differs from the intended joke"
    validate(written)

    print("Wrote %s (%d characters)" % (path, len(written)))


if __name__ == "__main__":
    main()
