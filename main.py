"""Everyday Things, Two Lines, Longer Run — entry generator.

Bounty: write a two-line entry (an everyday-thing analogy in line 1,
then what it maps and what it leaves out in line 2). Gate: 1-400
characters total, exactly 2 lines, no trailing newline. Writes the
entry to /output/entry.txt (UTF-8), with a read-back self-check.
"""

import os

TEXT = (
    "A traffic jam is like a line of ants where the first ant stops to smell a crumb, "
    "and every ant behind has to stop too, even though there's no crumb for them.\n"
    "The analogy maps how one small slowdown ripples backward into a full stop, "
    "but leaves out that cars can change lanes and ants can't."
)

MAX_LEN = 400

# Gate check: entry must be 1-400 characters (MAX_LEN) and exactly 2
# lines (one "\n"); a longer entry or a third line fails the bounty.
assert len(TEXT) <= MAX_LEN, f"entry too long: {len(TEXT)} > {MAX_LEN}"
assert TEXT.count("\n") == 1, "entry must be exactly 2 lines"


def main() -> str:
    candidates = ["/output/entry.txt", "./output/entry.txt"]
    written = None
    last_error = None
    for path in candidates:
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(TEXT)
            written = path
            break
        except OSError as exc:  # e.g. /output not writable; fall back
            last_error = exc
            continue
    if written is None:
        raise OSError(f"could not write entry to any candidate: {last_error}")

    # Read-back self-check: file must be byte-identical to TEXT.
    with open(written, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    assert back == TEXT, "read-back mismatch: file content differs from TEXT"
    assert not back.endswith("\n"), "entry must not end with a trailing newline"
    print(f"wrote {written}: {len(TEXT)} chars, {len(TEXT.encode('utf-8'))} bytes")
    return written


if __name__ == "__main__":
    main()
