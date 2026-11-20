#!/usr/bin/env python3
"""Draw Rider-Waite-Smith tarot cards from the bundled zh-TW deck.

Default: three distinct cards for the 過去 / 現在 / 建議 spread, each
independently upright (正位) or reversed (逆位).

Usage:
    python3 draw_tarot.py            # 3-card spread, readable text
    python3 draw_tarot.py --json     # same, as JSON
    python3 draw_tarot.py -n 1       # single card
    python3 draw_tarot.py --seed 42  # reproducible draw (for testing)
"""
import argparse
import json
import random
import sys
from pathlib import Path

DECK_PATH = Path(__file__).resolve().parent.parent / "assets" / "tarot_zhtw.json"
POSITIONS = ["過去", "現在", "建議"]
FIELDS = [
    ("meaning", "意義"),
    ("behavior", "行為"),
    ("marriage", "愛情"),
    ("sexuality", "兩性關係"),
    ("related", "相關詞"),
    ("star", "星座"),
]


def draw(n: int, rng: random.Random) -> list[dict]:
    deck = json.loads(DECK_PATH.read_text(encoding="utf-8"))
    ids = rng.sample(sorted(deck), n)
    cards = []
    for i, card_id in enumerate(ids):
        card = deck[card_id]
        upright = rng.random() < 0.5
        side = card["positive"] if upright else card["reversed"]
        cards.append({
            "position": POSITIONS[i] if n == 3 else f"第{i + 1}張",
            "id": card_id,
            "name": card["name"],
            "orientation": "正位" if upright else "逆位",
            "explain": card["explain"],
            **{key: side.get(key, "") for key, _ in FIELDS},
        })
    return cards


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-n", "--count", type=int, default=3, help="number of cards (1-78, default 3)")
    parser.add_argument("--seed", type=int, help="seed for a reproducible draw")
    parser.add_argument("--json", action="store_true", help="output JSON")
    args = parser.parse_args()

    if not 1 <= args.count <= 78:
        parser.error("--count must be between 1 and 78")

    rng = random.Random(args.seed) if args.seed is not None else random.SystemRandom()
    cards = draw(args.count, rng)

    if args.json:
        json.dump(cards, sys.stdout, ensure_ascii=False, indent=2)
        print()
        return 0

    print("抽牌結果：" + "、".join(f"{c['position']}－{c['name']}（{c['orientation']}）" for c in cards))
    for c in cards:
        print(f"\n## {c['position']}：{c['name']}（{c['orientation']}）")
        print(f"牌面解釋：{c['explain']}")
        for key, label in FIELDS:
            if c[key]:
                print(f"{label}：{c[key]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
