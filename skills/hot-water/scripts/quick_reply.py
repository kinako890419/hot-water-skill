#!/usr/bin/env python3
"""The hot-water bot's non-LLM replies, matching the original bot's rules.

Usage:
    python3 quick_reply.py reply "<message text>"   # keyword / random reply (may print nothing)
    python3 quick_reply.py fortune                 # 今日運勢

Rules for `reply`, checked in this order:
    contains 機器人         -> 蛤
    contains 好不好 / 要不要 -> random choice of 好 / 不要
    contains 熱水           -> 多喝熱水
    otherwise              -> ~11% chance of a random 多喝熱水/冷水 line, else silence
"""
import random
import sys

rng = random.SystemRandom()

# options

YES_NO = ["好", "不要"]
WATER = ["多喝熱水", "多喝冷水"]
DAILY_FORTUNE = [
    "不好吧",
    "今天宜多喝水",
    "今天宜多喝熱水",
    "今天宜多喝冷水",
    "今天宜多喝冰水",
    "今天宜多喝汽水",
    "今天宜多喝熱茶",
]


def reply(text: str) -> str:
    if "機器人" in text:
        return "蛤"
    if "好不好" in text or "要不要" in text:
        return rng.choice(YES_NO)
    if "熱水" in text:
        return "多喝熱水"
    if rng.randint(1, 100) >= 90:
        return rng.choice(WATER)
    return ""


def main(argv: list[str]) -> int:
    if not argv or argv[0] in {"-h", "--help"}:
        print(__doc__)
        return 0
    cmd = argv[0]
    if cmd == "reply":
        print(reply(" ".join(argv[1:])))
    elif cmd == "fortune":
        print(rng.choice(DAILY_FORTUNE))
    else:
        print(f"unknown command: {cmd}\n{__doc__}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
