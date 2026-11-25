"""One Line, One Laugh: Roast Your Fridge — make.fun entry.

A single fixed line roasting a fridge. The judge's brief, in order:
it is plainly about a fridge; it finds a specific detail worth
mocking (a smart fridge that watches the milk with a camera); it
turns on a twist (all that surveillance, and it still cannot see the
month-old leftovers plotting against its owner); and it reads well
out loud, landing on the last two words.

The grader runs this program twice with no network. Both runs must
leave the same bytes in $MAKEFUN_OUTPUT_DIR/entry.txt: the line is a
constant, so the output is deterministic by construction — no clock,
no randomness, no input other than the line itself. The line is also
printed to stdout, for the record, but the judged text is the file.
"""

import os


# One line, at most 200 characters: a smart fridge that spends its
# budget surveilling the milk with a camera, yet stays blind to the
# month-old leftovers quietly plotting against its owner inside it.
LINE = (
    "My fridge has Wi-Fi, a touchscreen and a camera that watches "
    "the milk, yet the leftovers from last month are still in there, "
    "quietly planning my funeral."
)

MAX_CHARS = 200


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "line must be 1-%d chars, got %d" % (MAX_CHARS, len(text))
        )
    if "\n" in text:
        raise SystemExit("line must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = text.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Verify the artifact the judge will read is exactly the line:
    # one line, no trailing newline, no extra bytes.
    with open(path, "rb") as f:
        if f.read() != data:
            raise SystemExit("written bytes do not match the line")
    print(text)


if __name__ == "__main__":
    main()
