"""Entry program: write one office joke to entry.txt.

The joke is a single line of UTF-8 text, 1 to 200 characters long.
The grader runs this program twice; both runs must write identical bytes.
"""

import hashlib
import os

TEXT = "I told my boss I'd finish the report by Friday. It's Friday. The report is a blank document called 'report_final_FINAL_v2.docx'."

# Gate contract: entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space, on a single line.
assert 1 <= len(TEXT) <= 200, "joke must be 1-200 characters"
assert TEXT.strip(), "joke must not be only white space"
assert "\n" not in TEXT and "\r" not in TEXT, "joke must be a single line"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = TEXT.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Read back and verify the written bytes match the intended text.
    with open(path, "rb") as f:
        written = f.read()
    assert written == data, "entry.txt content mismatch"
    # String-level round trip: the file must decode as UTF-8 to the
    # exact same joke, with no trailing whitespace added.
    assert written.decode("utf-8") == TEXT, "entry.txt text mismatch"
    assert written == written.rstrip(), "entry.txt has trailing whitespace"
    print(path)
    print(len(data))
    print(hashlib.sha256(data).hexdigest())


if __name__ == "__main__":
    main()
