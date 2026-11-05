# Local AI Privacy Hardening Guide

*A follow-up manual to the Local AI Handbook*

## Who this is for

If you followed the [Local AI Handbook](https://dylanasdale.github.io) and got a model running on your own machine — Ollama, LM Studio, Jan, or anything similar — congratulations. Your prompts and files are now (mostly) staying local, and that is a genuine privacy win.

But *mostly* is the word that matters. Local AI still leaves traces:

- The chat you deleted in the app may still be on disk somewhere.
- The model files you "removed" two months ago may still be in a cache folder eating 20 GB.
- The server that runs your model may be listening on a real network port, visible to every device on your coffee-shop Wi-Fi.
- Your shell history may quietly contain things you typed while debugging.

This manual is the step-by-step cleanup. It takes you from "it runs" to "it runs, and I know exactly what is on my disk and which doors are open." The whole thing is written in plain English, on the assumption you are comfortable copying commands into a terminal but not writing shell scripts from scratch.

## What is in here

| Page | What it covers |
|---|---|
| [01 · Ports and firewall rules](01-ports-and-firewall.md) | Which doors local AI opens, which to close, and why `127.0.0.1` is your safety word. |
| [02 · Model files and cache hygiene](02-model-files-and-cache-hygiene.md) | Where models and downloads pile up, and how to clear them safely. |
| [03 · Where chats persist on disk](03-where-chats-persist-on-disk.md) | The exact folders where your conversations are saved. |
| [04 · Autosave and screenshot risks](04-autosave-and-screenshot-risks.md) | Clipboard history, OS screenshots, and snippets that leak to the cloud. |
| [05 · Shell history hygiene](05-shell-history-hygiene.md) | What `~/.bash_history` remembers and how to make it forget. |
| [06 · The monthly privacy reset ritual](06-monthly-privacy-reset-ritual.md) | A fifteen-minute recurring routine to keep everything tidy. |
| [Hardening checklist](hardening-checklist.md) | A single printable checklist of every step in the manual. |
| [Glossary](glossary.md) | Plain-English definitions of the terms used here. |

## How to use this manual

1. Read pages 01 through 03 in order. That is the "know your exposure" part.
2. Work through pages 04 through 06 once, with the checklist open next to you.
3. Print (or bookmark) the checklist. Do the monthly reset ritual on a recurring date — the first Saturday of the month works well.

## What this is not

This is education, not a security audit, not legal advice, and not medical advice. Tools change their folder layouts and default settings between versions; paths here were written against the tool layouts common in 2026 and the manual tells you how to *find* the equivalent folder on your own machine. Your privacy risk depends on how you actually use AI — if your conversations contain real patient data, workers' names, or anything else sensitive, treat every app (local or cloud) as risky and talk to whoever governs your data policy.

---

Built and maintained by **Asdale Dynamics, LLC** · Licensed MIT · Part of [The Massive AI Manual](https://dylanasdale.github.io)
