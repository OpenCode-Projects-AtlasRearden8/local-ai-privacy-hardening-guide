# Hardening checklist

A one-page summary of every step in the manual. Print it, mark it, keep the pen nearby. Each entry links back to the full explanation.

## Setup (do once)

- [ ] Set every AI app server to `127.0.0.1` (pages [01](01-ports-and-firewall.md))
- [ ] Add firewall rules blocking inbound 11434, 1234, 8080, 8188, 7860
- [ ] Point each app at one shared models folder
- [ ] Create `models-manifest.md` and list current models
- [ ] Find each app's data path and write it in the manifest
- [ ] Prefer `.safetensors` / `.gguf` models over `.bin` / `.pth` from unknown publishers
- [ ] Exclude AI app data folder from OS desktop-search indexing
- [ ] Know whether your Desktop/Documents/Pictures folder cloud-syncs; decide if that is okay
- [ ] Use full-disk encryption if the machine leaves the house (or is shared)

## Monthly ritual (every month)

- [ ] Confirm listening ports bind `127.0.0.1` (page [06](06-monthly-privacy-reset-ritual.md))
- [ ] `du -sh` the model and cache folders; record sizes
- [ ] Delete models unused for 60+ days; update manifest
- [ ] Empty in-app chat trash; check data folder for orphans
- [ ] Clear AI app upload cache and vector store (if you used document attachments)
- [ ] Trim shell history (`sed` + `tail` filter, page [05](05-shell-history-hygiene.md))
- [ ] Clear clipboard history
- [ ] Delete screenshots older than a month (or move to a dated folder)

## Quarterly

- [ ] Delete chats older than 90 days
- [ ] Update AI apps; re-read storage-path settings after upgrades
- [ ] Refresh the manifest and checklist in a dated backup copy

## Before sharing anything

- [ ] Crop screenshots to the minimum window
- [ ] Blur or replace names, addresses, network IPs
- [ ] Confirm screenshot folder is not cloud-synced
