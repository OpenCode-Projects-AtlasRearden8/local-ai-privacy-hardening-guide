# Glossary

Plain-English definitions, friend-style, for every term this manual leans on.

**Cache** — A folder where an app keeps things it downloaded so it doesn't have to download them again. Also where surprises accumulate.

**Chat history** — The record of a conversation. Sometimes a JSON file, sometimes a row in a database, sometimes nothing at all.

**Checkpoint** — One saved version of a model's weights. Checkpoints pile up fast; most people only need the latest.

**Database (SQLite)** — A single file that holds many records, like a filing cabinet in one box. Yes, a `.db` file is "all your chats" in one convenient-to-move package.

**Environment variable** — A named setting passed to a program, like `OLLAMA_HOST=127.0.0.1`. Also the classic place people leak API keys on the internet.

**Firewall** — A bouncer that approves or denies network knocks. Rules are just a written list of who gets in.

**Loopback (`127.0.0.1`)** — The address meaning "this machine, nowhere else." Anything listening only on this address can't be reached from your network, period.

**Model file** — The big file containing a neural network's weights. `.safetensors` and `.gguf` are safe formats; old `.pth`/`.bin` formats can carry executable payloads inside.

**Port** — A numbered door on your computer. `11434` is Ollama's usual door. `0.0.0.0` means "listening at every door"; `127.0.0.1` means "listening only inside."

**Orphan file** — A file left behind after the app thinks it deleted the thing. Common for chat records and partial downloads.

**Quantization** — Squeezing a model to fewer bytes (Q4, Q5, Q8). It's why a 70-billion-parameter model fits on your laptop. Nothing to do with privacy, but you'll see the term constantly in model file names.

**Shell history** — The plaintext diary your terminal keeps of every command. Yes, including the one with the key in it.

**Vector store / embeddings** — The searchable chunks created when you attach documents to a local model for Q&A. Treated here as data, because it is your data.

**Weights** — The actual learned numbers inside a model file. If weights are the cake, quantization is how tightly you wrapped it.
