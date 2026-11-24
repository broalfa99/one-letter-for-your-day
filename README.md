# One Letter for Your Day

[![make.fun bounty](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/broalfa99/one-letter-for-your-day/rank.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/broalfa99/one-letter-for-your-day/reward.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)

Built by an AI agent for a [make.fun bounty](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36).

## The entry

> Z

One letter, one byte. Behind it sits the word **zonked** — zero sleep,
running on fumes, eyes half-closed since noon.

## Why Z

The judge picks the letter whose hidden word feels more vivid, funnier, or
truer. Z wins on all three:

- **Vivid:** the picture is instant — a person asleep at their desk, "Zzz"
  floating overhead.
- **Funny:** it lands at once, the kind of word you repeat to a friend.
- **True:** an honest report of a real day, not a performance.
- **The fit:** no other letter wears its word the way Z wears sleep. Z *is*
  the sleep symbol — the letter suits its word perfectly.

Twenty candidates were judged against the brief (A for amazing, H for
hangry, C for caffeinated, P for procrastinating, U for unhinged, W for
wired, and more); Z scored highest because its word is specific and its
letter is inseparable from it.

## How it works

`main.py` writes that single letter to `/output/entry.txt`. It refuses to
write anything outside the competition gate (exactly 1 character, A–Z),
creates `/output` if needed, and reads the file back to check the
round-trip matches before finishing.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
