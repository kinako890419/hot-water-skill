---
name: hot-water-tarot
description: Three-card Rider-Waite tarot reading (過去／現在／建議) in Traditional Chinese, from the 多喝熱水 hot-water bot's `!抽` command. Draws real random cards with a bundled script and the full zh-TW meanings for all 78 cards, then writes a structured reading of 500 characters or fewer. Use this whenever someone asks for 塔羅, 占卜, 抽牌, 抽一張, `!抽`, a tarot reading, or "draw cards for me", even if they only give a topic or a single keyword and not a full question.
---

# 熱水塔羅 (`!抽`)

Draw three cards and give a reading in Traditional Chinese. The cards are drawn with a script, not in your head, and the reading is based on the full zh-TW meanings of all 78 Rider-Waite tarot cards.

## 1. Get the question

Take the user's text and strip `!抽` / `！抽` and the spaces around it. What is left is the question.
- If it is a real question, answer that question.
- If it is not a question (a mood, a single word, or nothing at all), pick a keyword from it, or give a general reading for today, and read the cards for that. Don't ask a follow-up. The bot always answered in a single reply.

## 2. Draw the cards with the script, not in your head

```bash
python3 <skill-dir>/scripts/draw_tarot.py
```

Language models are bad at being random: they keep picking the same famous cards and keep them upright. The script draws 3 different cards out of 78 with real randomness. Each card is upright or reversed on a coin flip. It prints each card's position, name, orientation and its zh-TW meanings (意義, 行為, 愛情, 兩性關係, 相關詞, 星座) from `assets/tarot_zhtw.json`. Base the reading on those meanings. Use `--json` if you want structured output.

The card order is the spread:
- **左方（過去）**: the past that is shaping the present
- **中間（現在）**: the core issue right now
- **右方（建議）**: a direction to take from here

## 3. Write the reading

Write in Traditional Chinese, as an experienced Rider-Waite reader. 

<template>
**你抽到的牌是：<牌名（正/逆位）>、<牌名（正/逆位）>、<牌名（正/逆位）>**
---
**1. 內容分析**
- 過去｜<牌名 正/逆位>：<card meaning linked directly to the question, key point in **bold**>
  - {concrete, doable advice}
- 現在｜...
- 建議｜...
---
**2. 整體統整**
2.1 三張牌的關聯性與整體趨勢
2.2 建議執行的時間點與行動方案
2.3 需要特別注意的警訊
---
**3. 總結與建議**
{advice tied to the question}
</template>

Rules, with the reason for each:
- 500 characters or fewer in total.
- **About 50 characters per card** in 內容分析.
- **Every piece of advice must be something the person can actually do**, like "這週可以找兩三天休息一下" and not "保持正向". A vague reading feels like a template.
- Give the reading right away, in one reply, no follow-up questions.
