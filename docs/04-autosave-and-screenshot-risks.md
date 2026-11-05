# 04 · Autosave and screenshot risks

Some leaks don't come from the AI tool at all. They come from your operating system and desktop apps politely "helping" you preserve the past.

## Autosave: the quiet copyist

Your system probably keeps helpfully-rotated copies of things:

- **Clipboard managers** (many distros, Windows 10+ clipboard history, various Mac apps) remember screenshots and chat snippets you copied. Clear your clipboard history after pasting chat content into any other app.
- **Text editor autosave/backup files** — VS Code's "Hot Exit" and auto-save keep the file in memory *and* on disk if you paste chat content into a scratch file to read it later.
- **OS screenshots** land in known folders (e.g., `~/Pictures`, Desktop, or a "Captures" folder). Their names are predictable, so desktop search and third-party tools index them fast.
- **Cloud-synced Desktop/Documents.** If Microsoft OneDrive, iCloud, Dropbox, or Google Drive syncs these folders, a screenshot of your chat and a `.txt` of your notes are on someone else's server within seconds of you taking them.

## The screenshot checklist

Before you screenshot a chat (publishing a bug report, asking a friend, writing documentation):

1. **Crop, don't share the whole window.** Sidebars with other chat titles contain more than the question you mean to show.
2. **Blur or replace usernames and real names.** These show up in file names, tabs, and account panels.
3. **Check the URL bar.** `localhost:11434` may be mundane; `http://192.168.0.42:8080` tells a stranger your home network's address scheme.
4. **Think about what syncs where first.** Know where your OS stores screenshots and whether that folder is cloud-synced *before* you take the screenshot of anything sensitive.

## Snippets-of-you, indexed

Your OS has search (Windows Search/Spotlight/Tracker). These index your AI chats' exports, model file names, and screenshots, making content searchable from a desktop search bar. That is a feature — until someone else uses your computer. If your machine is shared with family or coworkers, consider:

- Excluding the AI app's data folder from desktop search indexing.
- Using a separate OS user account for high-sensitivity work.
- Full-disk encryption (BitLocker/FileVault/LUKS) so powered-off snapshots aren't stories waiting to be told.

## YouTube-and-friend leaks

If you *record* your screen for tutorials or bug reports:

- Have a "sensitive bin" folder per session, and move model lists, chat history, file paths, bookmarks, and passwords managers entirely out of frame before recording.
- Do not assume blur filters will catch everything; layout updates surprise everyone.

Next: what your terminal remembers.
