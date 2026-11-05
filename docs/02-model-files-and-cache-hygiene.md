# 02 · Model files and cache hygiene

Model files are the biggest chunk of local AI — multi-gigabyte files that get downloaded once and referenced forever. They also silently duplicate themselves in caches. Ten-minute download, three copies, 60 GB gone, and a folder full of models you no longer trust because you forgot which ones came from where.

## Where the files actually live

| App | Typical location |
|---|---|
| Ollama | `~/.ollama/models` |
| LM Studio | `~/.lmstudio/models` (older installs: `~/.cache/lm-studio/models`) |
| Hugging Face downloads | `~/.cache/huggingface/hub` |
| llama.cpp / misc | wherever you put the `.gguf` files |
| Jan | `~jan/models` (check the app's own settings page — it shows the path) |

(`~` means your home folder. On Windows, these live under `C:\Users\yourname\` with a dot-folder of the same name, usually with `AppData` variants.)

## Model-file formats: one small safety note

- **`.safetensors` and `.gguf`** are designed to hold just weights — loading them does not run arbitrary code. Good default.
- **Older `.bin` / `.pth` / `.pt` PyTorch files** can *execute code* when loaded, because the format can embed programs. Downloading a random one from a model hub is roughly like downloading a random `.exe` from a stranger's download page. If you must use one, prefer files hosted under official org accounts (e.g., `meta-llama`, `microsoft`) rather than re-uploads from unknown users.

## Cache hygiene routine

1. **List what you actually use.** For Ollama: `ollama list`. Anything you haven't touched in two months is a deletion candidate.
2. **Delete through the app when you can.** `ollama rm modelname`, or LM Studio's My Models → Delete. App-managed deletes also clean the metadata.
3. **Check the stragglers.** LM Studio sometimes leaves partial downloads; Hugging Face cache keeps old revisions. Look at `~/.cache/huggingface/hub` and remove folders for models you no longer use anywhere.
4. **Verify before you delete.** Search the folder name before removing it — deleting the wrong cache once teaches you to always search it afterward.
5. **Note sizes first.** `du -sh ~/.cache/huggingface` (Linux/macOS) or check folder properties on Windows. The number you save matters more than the speed you feel.

## Water-tight hygiene habits

- **One models folder per machine.** Don't scatter downloads across Downloads, Desktop, and AppData. Point each app at the same folder in its settings.
- **Keep a `models-manifest.md`** — a one-line note per model: name, where you downloaded it, why you keep it, and the date you last used it. Future-you will delete with confidence instead of hoarding out of doubt.
- **Treat prompt caches and vector databases as data.** RAG chunks and embeddings you built from work documents may be sitting in `~/.cache/` folders or app data directories. Include them in your monthly ritual.

Next: where your conversations themselves get saved.
