# 05 · Shell history hygiene

If you run local AI from a terminal, your shell is quietly keeping a diary. Every command you typed — including ones with file names, model tags, and occasionally an environment variable you really didn't mean to leave lying around — is sitting in a plain-text history file.

## Where the diary lives

| Shell | History file | Size cap |
|---|---|---|
| bash | `~/.bash_history` | `HISTSIZE` / `HISTFILESIZE` variables |
| zsh | `~/.zsh_history` | `HISTSIZE` / `SAVEHIST` variables |
| fish | `~/.local/share/fish/fish_history` | per-shell setting |
| PowerShell | `%APPDATA%\Microsoft\Windows\...\ConsoleHost_history.txt` | fixed by Windows |

## The three habits that matter

1. **Don't put secrets on the command line.** `export MY_API_KEY=sk-hunter2` typed once lives forever in plaintext. Use a `.env` file excluded via `.gitignore`, or your OS keyring.
2. **Purge the history when you're done with a sensitive session.**
   - bash: `history -c && history -w` (clears the running history and rewrites the file)
   - zsh: `rm ~/.zsh_history` then start a fresh shell
   - PowerShell: `Clear-History` (plus delete the `ConsoleHost_history.txt` file above for the file on disk)
3. **Start a shell without any history at all when you plan to type something embarrassing:** `bash --norc --noprofile`, or `HISTFILE=/dev/null bash`, or `env HISTSIZE=0 zsh`.

## Trim, don't just atomic-wipe

Blitzing your entire history loses useful things — the exact `ollama run` command with model flags that you keep forgetting, the `dd` command that fixed your USB stick. Instead, keep the useful lines and drop the rest:

```bash
# Remove lines containing model tags or anything remotely sensitive
sed -i '/sk-/d; /api[-_]key/d; /token=/d; /password/d' ~/.bash_history
# Then shrink any huge file down to the last 500 lines
tail -n 500 ~/.bash_history > /tmp/recent && mv /tmp/recent ~/.bash_history
```

In words: "Delete any history line containing an API-key pattern, a token, or a password — then keep only the most recent 500 lines." (Only do this to a file you *intend* to rewrite; the deletion pattern is a chainsaw.)

## History hygiene in plain English

- Your shell keeps **one copy** of your commands on disk for a reason: so you can reuse them. That same copy is also readable by anything with a shell on your machine, and readable in any backup you make of your home directory.
- You are not trying to zero-out everything; you are trying to make the *sensitive* entries forgettable while keeping the useful ones.
- If your home directory is backed up to anyone's server (NAS, cloud, Time Machine to a disk you haven't thought about), the history file goes with it — so a truly embarrassing entry follows you through every backup you keep. Purge early rather than purge never.

Next: the recurring ritual that maintans all of the above.
