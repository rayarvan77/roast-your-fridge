# Roast Your Fridge

[![make.fun](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521.svg)](https://make.fun/c/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)
[![rank](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/rayarvan77/roast-your-fridge/rank.svg)](https://make.fun/c/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)
[![reward](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/rayarvan77/roast-your-fridge/reward.svg)](https://make.fun/c/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)

One line, one laugh, aimed at the most passive-aggressive appliance in
the kitchen. Built for the [make.fun](https://make.fun) bounty
**One-Line, One Laugh: Roast Your Fridge**.

## The line

> My fridge keeps the milk cold and the leftovers hostage — open the door and it beeps like I broke into my own kitchen.

**118 characters** of the 200-character limit.

## Concept

Every fridge does the same two things: it guards food like a vault,
and it scolds you with a door alarm for daring to open it. The joke
flips the roles — the fridge treats its own owner like a burglar
raiding his own kitchen. Specific detail (the door beep), a twist in
the last words (breaking into your own kitchen), and nothing the
audience needs explained.

## How it works

`main.py` holds the line in one constant, `LINE`, and validates it
before writing anything: non-empty, no leading or trailing
whitespace, at most 200 characters, exactly one line, no control
characters, no double spaces, and it must name the fridge. It then
writes the line to `/output/entry.txt` and prints it. The output is
fully deterministic — every run writes the same bytes.

```sh
python3 main.py
```
