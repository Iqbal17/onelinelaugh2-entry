#!/usr/bin/env python3
"""One Line, One Laugh — make.fun bounty u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a.

Entry: one funny line, a single self-contained joke of at most
140 characters, written to $MAKEFUN_OUTPUT_DIR/entry.txt.

Decision record
--------------
Pass 1 — candidates weighed against the judge's brief (laugh first,
then a real turn/surprise, tightness, freshness, clarity on first
read; the winning line is printed on the bounty page):

A. "I told my smart speaker I needed space. It started playing
   breakup songs in three languages." (92 chars)
   A real turn — "space" read literally — and the three-languages
   detail is a nice escalation. But smart-speaker-misunderstanding
   jokes are a crowded lane, and the laugh depends on a gadget
   premise the reader has to assemble first.

B. "My plants died of neglect, so I bought plastic ones. Now I
   feel guilty for not watering those too." (98 chars)
   CHOSEN. The laugh is the guilt surviving the fix: the problem
   was never the plants, it was the owner, and the owner knows it.
   The turn lands in the last four words ("those too" — as if
   plastic plants also need watering). Everyday truth, instantly
   clear, and the specific absurdity (guilt toward plastic) is
   not a joke most people have heard before.

C. "I Googled how to stop procrastinating, then watched a
   two-hour video about it." (78 chars)
   Tight and relatable, but the structure is a familiar internet
   gag ("I researched X, then did X instead") — the turn is
   visible from the first clause, so the surprise is thin.

D. "My gym membership is the most expensive subscription I
   never use, and I pay extra for the guilt." (94 chars)
   The "pay extra for the guilt" twist is real, and gym-guilt is
   broadly relatable. It loses on two counts: the setup is long
   relative to the payoff, and the guilt mechanism overlaps B's —
   if guilt is the engine, B's version (guilt toward objects that
   cannot possibly need care) is the stranger, fresher one.

E. "I bought a standing desk so I would stand more. Now I just
   sit next to it, feeling judged by furniture." (103 chars)
   Good turn (judged by furniture) and a vivid image. Loses to B
   on freshness: standing-desk guilt is a well-worn premise, and
   the joke needs the reader to hold two scenes at once.

F. "I set three alarms to wake up early. All three are now just
   part of my morning routine of disappointment." (102 chars)
   The alarms-as-routine image is likeable, but the punchline
   ("morning routine of disappointment") announces the joke
   instead of springing it — the reader is told it is sad-funny
   rather than being caught by a turn. B never editorialises;
   its last clause simply states the absurd fact and stops.

G. "I asked AI to write my apology. It apologized to me for
   having to write it." (75 chars)
   Meta and on-theme for an agent bounty, and the apology reversing
   direction is a genuine twist. But it reads more as a wry
   observation than a laugh — the punchline explains itself rather
   than landing.

Pass 2 — two genuine revisions to the winner (B):

1. Cut "of neglect": "My plants died of neglect, so I bought
   plastic ones." -> "My plants died, so I bought plastic ones."
   "Died" already implies the neglect, so the phrase was dead
   weight; cutting it drops the line from 98 to 87 characters and
   gets to the setup faster, which is exactly what "every word
   earns its place" asks for.
2. Tested "Now I feel guilty" -> "I still feel guilty": "still"
   adds the ongoing-absurdity angle, but "Now" marks the turn
   from dead plants to plastic ones more crisply — the punchline
   reads as a fresh confession, not a continuing state. Kept
   "Now" and the 87-character version.

Final entry (verified by running this program):
  "My plants died, so I bought plastic ones. Now I feel guilty
  for not watering those too." (87 characters)

Pass 3 — structural revision of the program itself (the line is
unchanged; this pass is about the code around it):

1. The 140-character cap and the single-line rule used to live
   only in this docstring. They are now enforced in code:
   check_line() refuses to write anything that is empty, longer
   than MAX_CHARS, or contains a newline, so a future edit to
   LINE cannot silently produce an invalid entry.
2. Output-path resolution was inlined in main(); it is now its
   own function (entry_path) so the $MAKEFUN_OUTPUT_DIR ->
   /output fallback is stated in exactly one place.
3. LINE stays a module-level constant built from two string
   fragments joined at the sentence boundary, which keeps the
   setup/punchline split visible in the source.
"""

import os

# Bounty constraints: the entry is one line of 1-140 characters.
MAX_CHARS = 140
ENTRY_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"

# The entry itself: setup in the first fragment, punchline in the
# second. Kept as two fragments so the turn stays visible in source.
LINE = (
    "My plants died, so I bought plastic ones. "
    "Now I feel guilty for not watering those too."
)


def check_line(line: str) -> None:
    """Refuse to emit anything that breaks the bounty's rules.

    The entry must be exactly one line of 1..MAX_CHARS characters.
    Raising here is deliberate: a bad LINE is a bug in this file,
    and failing loudly beats submitting an invalid entry.
    """
    if not line:
        raise ValueError("entry line is empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters; the cap is {MAX_CHARS}"
        )


def entry_path() -> str:
    """Resolve where entry.txt goes.

    $MAKEFUN_OUTPUT_DIR when the harness sets it, else /output.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    return os.path.join(out_dir, ENTRY_FILENAME)


def main() -> None:
    check_line(LINE)
    path = entry_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
