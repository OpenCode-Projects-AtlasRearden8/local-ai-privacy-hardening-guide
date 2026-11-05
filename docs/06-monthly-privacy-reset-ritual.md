# 06 · The monthly privacy reset ritual

Hardening isn't a weekend; it's a rhythm. Once a month — fifteen minutes, coffee in hand — walk through this ritual. It's spelled out step by step. Done is better than perfect.

## The ritual, in order

### Part 1 · Doors (5 minutes)

1. List listening ports (`ss -tlnp` / `netstat -ano` / `lsof -iTCP -sTCP:LISTEN`). Confirm every AI-related one binds `127.0.0.1`.
2. If any app's server shows `0.0.0.0`, flip its host setting back before you forget which tutorial caused it.
3. Skim your firewall's rule list. Delete any rule you added for a tool you've since uninstalled.

### Part 2 · Files (5 minutes)

4. Run `du -sh` on your model folder and on `~/.cache/huggingface` (or the Windows equivalent). Note the numbers in `models-manifest.md`.
5. Delete models you haven't used in 60 days. Update the manifest as you go.
6. Empty the AI app's chat trash / deleted chats, and check for orphaned files in its data folder.
7. If the AI app attached or embedded documents this month, clear its upload cache and vector store.

### Part 3 · Memories (5 minutes)

8. Trim shell history with the sed/tail filter from page 05.
9. Clear clipboard history.
10. Move OS screenshots older than the month into a folder with an expiry date, or delete them.
11. Rotate the `models-manifest.md` into a dated copy if it's grown; delete stale manifest lines.

### Part 4 · The once-a-quarter extras

- Review chat history in your main app and delete anything over 90 days.
- Update each AI app. Read the release notes for storage-path changes — that's the #1 way your mental model drifts from disk reality.
- Back up your manifest + checklist. Don't back up chats/models.

## Making it stick

- Pick a fixed day: the first Saturday of the month has a nice rhythm to it.
- Stack it with something pleasant; coffee elevates any ritual.
- Print the [hardening checklist](hardening-checklist.md) and put a real pen mark on each item. Physical checkmarks work.
- If you miss a month: the ritual *is* the recovery. Just run the next one.
