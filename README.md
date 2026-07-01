# snippets

Small, reusable Python & shell utilities I reach for often. Each lives in one file,
no dependencies, copy-paste friendly.

## Contents
- `slugify.py` — turn any string into a URL-safe slug
- `retry.py` — retry a flaky call with exponential backoff
- `humanize_bytes.py` — human-readable byte sizes (1536 -> '1.5 KiB')
- `chunk.py` — split an iterable into fixed-size chunks
- `timer.py` — context manager that prints elapsed wall time
- `load_env.py` — tiny .env parser into a dict
- `parallel_map.py` — thread-pooled map for I/O-bound work
- `deep_get.py` — safe nested lookup by dotted path
- `dedupe.py` — order-preserving dedupe with optional key
- `sh.py` — run a command, return stripped stdout
- `truncate.py` — truncate to n chars on a word boundary
