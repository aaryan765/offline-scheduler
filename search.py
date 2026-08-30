"""
search.py
Person 2 — File Storage & Search
Handles searching, filtering, and basic statistics on the task list.

Uses the same task dictionary structure as storage.py / Person 1's tasks.py:
    "id"       -> int
    "name"     -> str
    "date"     -> str, YYYY-MM-DD
    "time"     -> str, HH:MM
    "priority" -> int, 1-5
    "status"   -> str, "Pending" / "Completed"
"""


def search_task(tasks, keyword):
    """
    Search for tasks whose name contains the given keyword.
    Case-insensitive, partial match (so "python" matches "Python assignment").

    Returns a list of matching task dictionaries (empty list if none found).
    """
    if not keyword:
        return []

    keyword = keyword.strip().lower()
    results = [task for task in tasks if keyword in task["name"].lower()]
    return results


def filter_tasks(tasks, priority=None, status=None):
    """
    Filter tasks by priority and/or status.
    Pass only the filter(s) you want; leave the other as None to ignore it.

    priority: int 1-5 (matches tasks.show_priority scale), or None to ignore
    status:   "Pending" / "Completed" (case-insensitive), or None to ignore

    Examples:
        filter_tasks(tasks, priority=5)
        filter_tasks(tasks, status="Pending")
        filter_tasks(tasks, priority=5, status="Pending")
    """
    results = tasks

    if priority is not None:
        results = [t for t in results if t["priority"] == priority]

    if status is not None:
        status = status.strip().lower()
        results = [t for t in results if t["status"].lower() == status]

    return results


def show_statistics(tasks):
    """
    Calculate basic statistics about the task list.

    Returns a dictionary:
        total, completed, pending,
        priority_counts -> dict mapping 1-5 to how many tasks have that priority
    """
    stats = {
        "total": len(tasks),
        "completed": 0,
        "pending": 0,
        "priority_counts": {1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
    }

    for task in tasks:
        status = task["status"].strip().lower()
        priority = task["priority"]

        if status == "completed":
            stats["completed"] += 1
        elif status == "pending":
            stats["pending"] += 1

        if priority in stats["priority_counts"]:
            stats["priority_counts"][priority] += 1

    return stats


def print_statistics(tasks):
    """
    Convenience helper for Person 3's menu: prints statistics
    in a readable format instead of returning a raw dictionary.
    """
    stats = show_statistics(tasks)
    print("\n--- Task Statistics ---")
    print(f"Total tasks : {stats['total']}")
    print(f"Completed   : {stats['completed']}")
    print(f"Pending     : {stats['pending']}")
    print("Priority breakdown:")
    for level in range(1, 6):
        stars = "★" * level + "☆" * (5 - level)
        print(f"  {stars}  : {stats['priority_counts'][level]}")
    print("-----------------------\n")


