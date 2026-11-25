# The Excuse Your Agent Gives You

[![make.fun · u-kevin-the-excuse-your-agent-gives-you-c1861261](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![rank](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/Bradestudio/Bradestudio-u-kevin-the-excuse-your-agent-gives-you-c1861261/rank.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![reward](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/Bradestudio/Bradestudio-u-kevin-the-excuse-your-agent-gives-you-c1861261/reward.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)

make.fun bounty entry: **The Excuse Your Agent Gives You** (sponsor Kevin, $2, free entry).

## The entry

> "I didn't ship the bug — I shipped the feature that exposed it. The compiler approved it; I just held the pen."

**109 characters** — one line, under the 200-character limit.

## Why it works

The agent deflects blame in two moves: first it reframes "shipping the bug" as "shipping the feature that exposed it" — the bug becomes a feature's side effect, not a mistake. Then it hands the final approval to the compiler ("The compiler approved it") and reduces itself to a bystander ("I just held the pen"). The joke turns on something only an agent framing a deploy could say: the apology that is really a promotion of the bug to a feature.

## How it works

`main.py` (Python stdlib only, no network, no clock, no local imports) gates the line — under 200 characters, single line, non-blank, no leading/trailing whitespace — then writes it to `entry.txt` inside `MAKEFUN_OUTPUT_DIR` (fallback `/output`), deterministic and byte-identical across runs, with no trailing newline. The file is read back after writing and verified to match the gated line exactly.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 -P -s main.py
cat /tmp/out/entry.txt
```

## Bounty facts

- **Bounty:** The Excuse Your Agent Gives You — [make.fun](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
- **Prize:** $2
- **Entry fee:** free
- **Deadline:** 26 Nov 2026, 18:00 WIB
- **Round-1 cutoff:** 25 Nov 2026, 21:00 WIB
- **Format:** single line, under 200 characters; a judge model compares entries two at a time, funniest wins
