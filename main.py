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

E. "I bought a standing desk so I would stand more. Now I just
   sit next to it, feeling judged by furniture." (103 chars)
   Good turn (judged by furniture) and a vivid image. Loses to B
   on freshness: standing-desk guilt is a well-worn premise, and
   the joke needs the reader to hold two scenes at once.

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
"""

import os

LINE = (
    "My plants died, so I bought plastic ones. "
    "Now I feel guilty for not watering those too."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
