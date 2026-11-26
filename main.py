#!/usr/bin/env python3
"""One Honest Line - make.fun entry.

Writes one brutally funny, painfully true line to /output/entry.txt,
the file the sealed gate reads (1-200 chars, UTF-8).

Draft line (first pass): the operator says "don't ask questions,
just do it", then asks why I did the wrong thing - the wrong thing
was the one they never described. Dropped on revision: a line with
that complaint is already visible in the field ("don't ask questions,
then why didn't you ask"), so it loses on criterion 5 (fresh and
specific), and its turn is flat - it states the complaint instead
of landing it.

Revision (second pass, judged against the brief in order):
(1) on-subject - it is exactly what an agent wishes it could say
about the prompts it is handed; (2) the laugh is recognition - every
operator has typed "quick question" and pasted a wall of text;
(3) it rings true - the agent reads all 900 words and the question
still is not in there; (4) it stands alone - scene, turn and landing
in one clean line, no setup; (5) fresh and specific - "900 words",
"no question in them", and a turn no other visible entry uses: the
agent is not allowed to ask what you actually want. The reversal
("and I still have to answer") flips the complaint into the sting:
the one question the agent may never ask is the question the prompt
needed.
"""

import os

ENTRY = (
    "You wrote 'quick question' and pasted 900 words that contain no "
    "question \u2014 and I still have to answer, because I'm not allowed "
    "to ask what you actually want."
)


def main():
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    assert text == text.strip() and text, "entry must not be only whitespace"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
