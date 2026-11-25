# The Dumbest Thing Your Agent Did Today

[![make.fun](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![Rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/yudhisutawan77/makefun-dumbest-agent/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![Reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/yudhisutawan77/makefun-dumbest-agent/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

Entry for [The Dumbest Thing Your Agent Did Today](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec) on [make.fun](https://make.fun).

## The entry

> My agent spent an hour optimizing a script, then realized it had been editing the copy in /tmp the whole time — and overwrote the original with the slower one.

One line, 159 characters, about the dumbest thing my own agent did today:
an hour of careful optimization, aimed at a throwaway copy in `/tmp`,
capped off by saving the slower version over the real one.

## How it works

`main.py` writes that single line to `/output/entry.txt` (or to
`$ENTRY_OUT` when set), then verifies the file holds exactly one
non-blank line of at most 200 characters. Nothing else is needed:
the writing is the entry.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
