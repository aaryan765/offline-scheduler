"""Tests for search.py — search_task, filter_tasks, show_statistics."""

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import search

SAMPLE_TASKS = [
    {"id": 1, "name": "Complete Python assignment", "date": "2026-08-28",
     "time": "18:30", "priority": 4, "status": "Pending"},
    {"id": 2, "name": "Buy groceries", "date": "2026-08-29",
     "time": "10:00", "priority": 1, "status": "Completed"},
    {"id": 3, "name": "Team meeting prep", "date": "2026-08-29",
     "time": "15:00", "priority": 4, "status": "Pending"},
]


class TestSearchTask(unittest.TestCase):
    def test_finds_matching_name_case_insensitive(self):
        results = search.search_task(SAMPLE_TASKS, "PYTHON")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["id"], 1)

    def test_partial_match_works(self):
        results = search.search_task(SAMPLE_TASKS, "meet")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Team meeting prep")

    def test_no_match_returns_empty_list(self):
        results = search.search_task(SAMPLE_TASKS, "nonexistent")
        self.assertEqual(results, [])

    def test_empty_keyword_returns_empty_list(self):
        results = search.search_task(SAMPLE_TASKS, "")
        self.assertEqual(results, [])


class TestFilterTasks(unittest.TestCase):
    def test_filter_by_priority_only(self):
        results = search.filter_tasks(SAMPLE_TASKS, priority=4)
        self.assertEqual(len(results), 2)
        for task in results:
            self.assertEqual(task["priority"], 4)

    def test_filter_by_status_only(self):
        results = search.filter_tasks(SAMPLE_TASKS, status="Completed")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["id"], 2)

    def test_filter_by_status_is_case_insensitive(self):
        results = search.filter_tasks(SAMPLE_TASKS, status="completed")
        self.assertEqual(len(results), 1)

    def test_filter_by_priority_and_status_together(self):
        results = search.filter_tasks(SAMPLE_TASKS, priority=4, status="Pending")
        self.assertEqual(len(results), 2)

    def test_no_filters_returns_all_tasks(self):
        results = search.filter_tasks(SAMPLE_TASKS)
        self.assertEqual(len(results), 3)


class TestStatistics(unittest.TestCase):
    def test_show_statistics_counts_correctly(self):
        stats = search.show_statistics(SAMPLE_TASKS)
        self.assertEqual(stats["total"], 3)
        self.assertEqual(stats["completed"], 1)
        self.assertEqual(stats["pending"], 2)
        self.assertEqual(stats["priority_counts"][4], 2)
        self.assertEqual(stats["priority_counts"][1], 1)

    def test_show_statistics_on_empty_list(self):
        stats = search.show_statistics([])
        self.assertEqual(stats["total"], 0)
        self.assertEqual(stats["completed"], 0)
        self.assertEqual(stats["pending"], 0)

    def test_print_statistics_does_not_crash(self):
        try:
            search.print_statistics(SAMPLE_TASKS)
            search.print_statistics([])
        except Exception as e:  # noqa: BLE001
            self.fail(f"print_statistics raised {type(e).__name__}: {e}")


if __name__ == "__main__":
    unittest.main()
