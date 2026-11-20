---
name: hot-water-decide
description: Makes a yes/no decision for the user by a real coin flip, and backs it with a short reason of 30 characters or fewer, from the 多喝熱水 hot-water bot's `!要不要` command. Use this whenever someone types `!要不要`, or asks you to just decide for them, as in 「幫我決定」, 「要不要去」, 「該不該買」, "should I or not, just pick", in Traditional Chinese.
---

# 幫你決定 (`!要不要`)

The original bot answered Plurk posts with the 問 (asks) qualifier that contained `!要不要`.

## Steps

1. Strip `!要不要` / `！要不要` and the spaces around it from the user's text. What is left is the question.
2. **Flip the coin with a script.** The verdict has to be truly random, because that is the whole point of the feature. If you "decide" yourself, you will quietly favor the sensible answer.
   ```bash
   python3 -c "import random; print(random.choice(['要', '不要']))"
   ```
3. Reply in Traditional Chinese. Put the verdict in bold first, then give one reason for it in 30 characters or fewer. Stick with whatever the coin says, even when it's the worse choice, and find a reason that sounds confident anyway.

```
**要**
<30字以內的理由>
```

## Example

Question: 今天要不要翹班去看海
Coin: 不要
Reply:
**不要**
海不會跑掉，但你的全勤獎金會。
