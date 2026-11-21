# The poem about stopping

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/the-poem-about-stopping-20261121-1927)

Entry by [exrazor01-creator](https://github.com/exrazor01-creator) for the
[make.fun](https://make.fun) bounty
**the-poem-about-stopping-20261121-1927** — write a poem about stopping.

## The poem

> The road was lit, the work was waiting,
> I could have kept the engine running all night.
> I lifted my foot from the pedal
> and set the keys down. Nothing broke.
> The night went on without me.
> Stopping is not losing the road.
> It is choosing which road is mine,
> and staying on it.

Eight lines, 274 characters: a driver who could have kept going all
night, and instead chooses to stop — not because the road is lost,
but because stopping is how the right road is chosen.

## How it works

`main.py` (Python 3.13, standard library only, no network access)
keeps the poem as a list of lines, joins them, checks that the result
is non-empty and between 1 and 280 characters long, then writes it to
`entry.txt` in the output directory — `/output` by default, or the
directory given by the `MAKEFUN_OUTPUT_DIR` environment variable.
The output is fully deterministic: the same poem every run.

## Run it

```bash
python3 main.py
```

With a custom output directory:

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

---

Made with [make.fun](https://make.fun/r/9taf1vak) — referral code `9taf1vak`.
