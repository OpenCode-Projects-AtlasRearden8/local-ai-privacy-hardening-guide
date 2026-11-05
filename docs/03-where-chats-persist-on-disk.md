# 03 · Where chats persist on disk

Deleting a conversation in the app's sidebar does not necessarily delete what is on disk. Each tool saves chats in a slightly different place, and some keep exports, logs, or a database even after you click delete. This page tells you where to look.

## The natural habitat of each tool

| App | Chats typically live at | Notes |
|---|---|---|
| LM Studio | `~/.lmstudio/` (Chats & My Models are subfolders; check the app's *Data Path* setting) | The app shows its data path on the welcome/settings screen — the single most useful thing to know. |
| Ollama (CLI) | Not stored persistently by default | A terminal conversation vanishes when the terminal dies. If you pipe it to a file, *that file* is your memory now. |
| Open WebUI | A SQLite database (often `webui.db`) inside its data folder | Chats, files you attached, and accounts all live in one database file. Delete the file and the whole interface's memory is gone. |
| Jan | `~/.jan/` (check its Settings → General) | Chats plus app-specific assistant configs. |
| llama.cpp / scripts | Whatever you redirect output to | `---` nothing auto-saved. |

## Reading the leftovers

Even after deleting in-app, some apps keep:

- **Orphaned chat JSON files** in the data folder (LM Studio in particular: deleting via UI should clean these, but check the folder after a version upgrade).
- **Vector indexes / RAG caches** — chunks of any documents you attached for Q&A. These may have full sentences from your files, in plain text.
- **OS-level copies**: your text editor's autosave, clipboard managers, and desktop search indexes.

## Practical habits

- **Know your app's data path.** Open settings, find the "data" or "storage" line, and write it down in your `models-manifest.md`. Every app has one; every guide avoids telling you.
- **Delete inside the app, then verify.** Delete a test chat, then search its data folder for a distinguishing word from that chat. If the word is still there, you know it keeps shadows, and your monthly ritual should include that folder.
- **Treat attached documents like the chats themselves.** If you attach your résumé to ask a model to rewrite it, the attachment, its extracted text, and the chat reply may all persist.
- **Back up nothing sensitive by default.** Local backups are your choice; sync-to-cloud backups of your entire home folder (OneDrive, iCloud Desktop) will carry your chats with them. That is page 04's territory.

Next: the sneaky leak paths — autosave and screenshots.
