# 01 · Ports and firewall rules

Every desktop AI app quietly opens a *port* — a numbered door on your computer that programs use to talk to each other. If that door is left facing the internet (or even the rest of your home network), other people can use your chat models, read your history in some setups, and generally poke at a machine you thought was private.

## The one rule that fixes most of this

Local AI servers should listen on `127.0.0.1` — the *loopback* address, which means "this machine only." Nothing outside your computer can reach a loopback-hosted service, firewall or no firewall.

- **Ollama:** set the environment variable `OLLAMA_HOST=127.0.0.1` (this is the default on most installs, but it gets changed surprisingly often by tutorials that want you to share across your house).
- **LM Studio:** Developer tab → the server has a "Host" setting. If it says `0.0.0.0`, every device on your network can reach it.
- **Open WebUI, Jan, ComfyUI, text-generation-webui:** each has a host/bind setting; anything that says `0.0.0.0` or your LAN IP is a door standing open.

Plain-English version: `0.0.0.0` means "listen at every door in the building." `127.0.0.1` means "listen only at the door inside my own office."

## Common ports, and what to do with them

| Port | Usually is | Keep open? |
|---|---|---|
| 11434 | Ollama API | Yes — bound to 127.0.0.1 |
| 1234 | LM Studio local server | Yes — bound to 127.0.0.1 |
| 8080 | Open WebUI (and many, many other things) | Yes — bound to 127.0.0.1 |
| 8188 | ComfyUI | Yes — bound to 127.0.0.1. If you use tunnels/cloud proxies, stop. |
| 7860 | Gradio apps, text-generation-webui | Yes — bound to 127.0.0.1 |
| 5000, 3000 | Local web front-ends | Caution — double-check they are loopback-only |
| 22 | SSH on Linux/macOS | Your call — not AI related, but know it exists |

You are *not* trying to close the ports your local AI legitimately needs. You are making sure each one is reachable only from your own machine.

## Firewall rules, in plain English

A firewall is a bouncer. It checks each knock at each door against a rule list. The rules below are phrased as the operating system would enforce them, then in words.

**Linux (ufw):**

```bash
# Deny others from reaching your local-AI ports
sudo ufw deny 11434
sudo ufw deny 1234
sudo ufw deny 8080
sudo ufw deny 8188
sudo ufw deny 7860
sudo ufw status verbose
```

In words: "Nobody outside this machine may knock on these five doors." Loopback traffic is unaffected — your own apps can still use Ollama locally.

**macOS:** System Settings → Network → Firewall → Options. Add each AI app (ollama, LM Studio, llamacpp) and set it to *Block incoming connections*. In words: "This app may start conversations, but may not receive knocks."

**Windows:** `wf.msc` → Inbound Rules → New Rule → Port → the specific port numbers above → Block. In words: same as Linux, but the bouncer checks Windows' own list.

One honest note: strictly speaking, a loopback-bound service cannot be reached from the network at all, so the deny rules are a *second seat belt with air bags*. That is exactly the spirit of hardening — assume you'll one day flip a setting for a tutorial and not remember to flip it back.

## Things to check once a month

1. Run `netstat` (Windows), `ss -tlnp` (Linux), or `lsof -iTCP -sTCP:LISTEN` on the Mac. Look for ports belonging to your AI apps and confirm the local address starts with `127.0.0.1`.
2. Anything listening on `0.0.0.0` or `192.168.x.x` is worth investigating.
3. If you don't recognize what owns a listening port, search the process name before you stop it.

Next up: where the model files themselves live, and how to clean out the ones you're done with.
