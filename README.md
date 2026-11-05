# Local AI Privacy Hardening Guide

*A follow-up manual for people who already run local AI — locking down ports, caches, chat history, and the small leaks nobody warns you about.*

By **Asdale Dynamics, LLC** — part of [The Massive AI Manual](https://dylanasdale.github.io) family: AI explained like a friend would. Plain English, step by step, never condescending.

## What this is

You got a local model running. Great — that's the privacy win. But "local" isn't automatically "private." Chats still get written to disk somewhere. Model files pile up in caches. The server that runs your model may be listening on a port your whole coffee-shop Wi-Fi can reach. Your shell history remembers everything you typed while debugging.

This manual is the follow-up: a plain-English hardening guide covering:

- **Ports and firewall rules** — which doors local AI opens, and how to make sure each one only opens inward. Written both as real commands and in plain English.
- **Model-file and cache hygiene** — where the multi-gigabyte files actually live, which formats are safe (`.safetensors`/`.gguf` vs old `.pth`/`.bin`), and a deletion routine that won't surprise you.
- **Where chats persist on disk** — the data folders LM Studio, Ollama, Open WebUI, and Jan use, and how to verify a "deleted" chat is really gone.
- **Autosave and screenshot risks** — clipboard managers, OS screenshots, dashboards, and cloud-synced Desktop folders.
- **Shell history hygiene** — trimming `~/.bash_history` and friends without losing the useful lines.
- **A monthly privacy reset ritual** — a fifteen-minute recurring routine, plus a printable hardening checklist and glossary.

Education only — not security, legal, or medical advice.

## Reading it

- **Online/static site:** the `site/` folder contains the built HTML. Build it yourself with:

  ```bash
  python3 scripts/build.py     # renders docs/*.md -> site/*.html
  python3 tests/test.py        # runs the build tests
  ```

  No dependencies that matter: Python 3.9+. If the `markdown` package is installed it is used; otherwise a built-in fallback renderer takes over (the tests cover both paths).

- **In a markdown viewer / on GitHub:** read the `docs/` folder directly. Start with `docs/index.md`.

## Getting set up for contributions

Nothing to install beyond Python. Recommended checks before submitting a PR:

```bash
python3 tests/test.py && python3 -m unittest discover -s tests -p "test.py"
```

## Repo layout

```
docs/                      the manual, in markdown (source of truth)
scripts/build.py           markdown -> HTML site builder (stdlib + optional `markdown`)
tests/test.py              build/verification tests
assets/style.css           shared stylesheet, copied into site/ at build time
site/                      generated static site (regenerate, don't hand-edit)
```

## License

MIT — see [LICENSE](LICENSE). Copyright (c) 2026 Asdale Dynamics, LLC.

## Disclaimer

This project is educational. Tool layouts change between versions; every page tells you how to *find* the equivalent folder or setting on your own machine. Your privacy posture depends on how you actually use these tools — treat every app (local or cloud) as risky when the material is sensitive.
