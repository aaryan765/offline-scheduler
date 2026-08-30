"""
storage.py
Person 2 — File Storage & Search
Handles saving tasks to a local text file and loading them back.

Task data structure (matches Person 1's tasks.py exactly):
Each task is a dictionary with these keys:
    "id"       -> int
    "name"     -> str
    "date"     -> str, format YYYY-MM-DD
    "time"     -> str, format HH:MM (24-hour)
    "priority" -> int, 1-5 (1 = lowest, 5 = highest, see tasks.show_priority)
    "status"   -> str, "Pending" / "Completed"

Person 1's tasks.py keeps tasks in a single module-level list called
`tasks`. This module does NOT hold its own copy of that list - you pass
it in and get it back, e.g. in main.py:

    import tasks as task_module
    import storage

    task_module.tasks = storage.load_tasks()      # on startup
    ...
    storage.save_tasks(task_module.tasks)          # after any change

File format:
Plain text file, one task per line, fields separated by "|":
    id|name|date|time|priority|status

Example line:
    1|Complete Python assignment|2026-08-28|18:30|4|Pending
"""

FILENAME = "tasks.txt"
DELIMITER = "|"


def save_tasks(tasks, filename=FILENAME):
    """
    Save a list of task dictionaries to a text file.
    Overwrites the file each time it is called, so it should be
    called after every change (add, complete, delete).

    Returns True if saving succeeded, False otherwise.
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for task in tasks:
                line = DELIMITER.join([
                    str(task["id"]),
                    str(task["name"]),
                    str(task["date"]),
                    str(task["time"]),
                    str(task["priority"]),
                    str(task["status"]),
                ])
                f.write(line + "\n")
        return True
    except (OSError, KeyError) as error:
        print(f"Error saving tasks: {error}")
        return False


def load_tasks(filename=FILENAME):
    """
    Load tasks from a text file and return them as a list of
    dictionaries. If the file does not exist yet (first run) or is
    empty, an empty list is returned instead of crashing.
    """
    tasks = []

    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        # Normal on first run - no tasks saved yet.
        return tasks

    for line_number, raw_line in enumerate(lines, start=1):
        line = raw_line.strip()
        if not line:
            continue  # skip blank lines

        parts = line.split(DELIMITER)
        if len(parts) != 6:
            print(f"Skipping malformed line {line_number} in {filename}")
            continue

        task_id, name, date, time, priority, status = parts

        try:
            task_id = int(task_id)
        except ValueError:
            print(f"Skipping line {line_number}: invalid task ID")
            continue

        try:
            priority = int(priority)
        except ValueError:
            print(f"Skipping line {line_number}: invalid priority")
            continue

        tasks.append({
            "id": task_id,
            "name": name,
            "date": date,
            "time": time,
            "priority": priority,
            "status": status,
        })

    return tasks
