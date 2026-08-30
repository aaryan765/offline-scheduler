# STDLIB.md — Package → Standard Library Substitution Log

Offline Smart Scheduler has **zero third-party runtime dependencies**
(`requirements.txt` is intentionally empty). This document lists
common packages a typical implementation of this kind of tool would
reach for, and what standard-library functionality was used instead
across `main.py`, `interface.py`, `tasks.py`, `storage.py`, and
`search.py`.

| # | Normally would use | Instead we used | Where in this project |
|---|---|---|---|
| 1 | `SQLAlchemy`, `sqlite3` ORM wrappers, or `TinyDB` | Plain text file I/O with `open()`, a hand-rolled `\|`-delimited line format, `str.split()` / `str.join()` | `storage.py` — `save_tasks()` writes one task per line as `id\|name\|date\|time\|priority\|status`; `load_tasks()` parses it back, skipping malformed lines instead of crashing |
| 2 | `click` / `typer` / `argparse`-based CLI frameworks | Plain `input()` / `print()` menu loop | `interface.py` — `show_menu()`, `get_choice()`, `get_filter()` drive the whole CLI with no framework |
| 3 | `python-dateutil` / `pendulum` for date handling | Dates and times are kept and compared as plain strings (`"YYYY-MM-DD"`, `"HH:MM"`) — no third-party parser needed because the project never needs calendar arithmetic, only storage and display | `tasks.py` (`add_task()`), `storage.py` (task dict fields) |
| 4 | `tabulate` / `prettytable` for table output | Manual `print()` formatting with fixed separator lines | `tasks.py` — `view_tasks()`; `interface.py` — `display_results()` |
| 5 | `fuzzywuzzy` / `rapidfuzz` for search | Plain substring matching via the `in` operator on `str.lower()` | `search.py` — `search_task()` |
| 6 | `pandas` for filtering / groupby-style stats | Plain list comprehensions and manual counting with a dict accumulator | `search.py` — `filter_tasks()` (priority/status filtering) and `show_statistics()` / `print_statistics()` (totals, completed/pending counts, priority breakdown) |
| 7 | `colorama` / `rich` for colored/styled terminal output | Unicode star characters (`★`/`☆`) built with plain string multiplication, no ANSI color codes needed | `tasks.py` — `show_priority()`; `interface.py` — `display_results()` |
| 8 | `pydantic` / `attrs` / a custom ORM model class | Plain `dict` objects, one per task, with a fixed set of keys (`id`, `name`, `date`, `time`, `priority`, `status`) | `tasks.py` — the module-level `tasks` list holds dicts built in `add_task()` |
| 9 | `pytest` (+ plugins like `pytest-mock`) | `unittest` and `unittest.mock` (both stdlib) | `tests/` — automated suite, including mocking `input()` for the interactive functions in `tasks.py` and `interface.py` |

## Design notes

- **No `json` or `csv` module either.** Even though both are stdlib
  and would have been "free," we chose an even simpler hand-rolled
  `|`-delimited format for `storage.py` — one line per task, split on
  a fixed delimiter. This keeps the file human-readable and trivial
  to debug by eye, at the cost of needing our own malformed-line
  handling (see `load_tasks()`), which we implemented and test for
  directly.
- **Priority is a plain `int` (1–5)**, rendered as stars via string
  repetition (`"★" * priority`) rather than any formatting library.
- **Task IDs are assigned manually** (`tasks[-1]["id"] + 1` in
  `tasks.py`) instead of relying on a database's auto-increment.

## Verification

No `import` statement anywhere in `main.py`, `interface.py`,
`tasks.py`, `storage.py`, or `search.py` references a third-party
package — only each other (local modules) and the Python standard
library (`unittest`, `unittest.mock` in tests). This can be verified
by running the project directly:

```
python main.py
```

No `pip install` step is required or possible, since `requirements.txt`
is empty.
