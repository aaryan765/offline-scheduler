"""
Tests for tasks.py — add_task, view_tasks, complete_task, delete_task,
change_priority, show_priority.

tasks.py's functions are interactive (they call input() directly)
rather than taking arguments, so these tests use unittest.mock.patch
to feed simulated keyboard input — this is a standard-library
technique (unittest.mock), not a third-party dependency.

Each test resets the module-level `tasks` list first, since tasks.py
keeps state in a shared list rather than passing it around.
"""

import os
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import tasks


class TestShowPriority(unittest.TestCase):
    def test_star_ratings_at_each_level(self):
        self.assertEqual(tasks.show_priority(1), "★☆☆☆☆")
        self.assertEqual(tasks.show_priority(3), "★★★☆☆")
        self.assertEqual(tasks.show_priority(5), "★★★★★")


class TestAddTask(unittest.TestCase):
    def setUp(self):
        tasks.tasks = []

    @patch("builtins.input", side_effect=[
        "Complete Python assignment", "2026-08-28", "18:30", "4"
    ])
    def test_add_task_creates_task_with_id_1(self, mock_input):
        tasks.add_task()
        self.assertEqual(len(tasks.tasks), 1)
        self.assertEqual(tasks.tasks[0]["id"], 1)
        self.assertEqual(tasks.tasks[0]["name"], "Complete Python assignment")
        self.assertEqual(tasks.tasks[0]["priority"], 4)
        self.assertEqual(tasks.tasks[0]["status"], "Pending")

    @patch("builtins.input", side_effect=[
        "First task", "2026-08-28", "18:30", "3",
        "Second task", "2026-08-29", "09:00", "2",
    ])
    def test_second_task_gets_incremented_id(self, mock_input):
        tasks.add_task()
        tasks.add_task()
        self.assertEqual(tasks.tasks[0]["id"], 1)
        self.assertEqual(tasks.tasks[1]["id"], 2)

    @patch("builtins.input", side_effect=[
        "Bad priority task", "2026-08-28", "18:30", "9"
    ])
    def test_out_of_range_priority_is_rejected(self, mock_input):
        tasks.add_task()
        self.assertEqual(len(tasks.tasks), 0)

    @patch("builtins.input", side_effect=[
        "Bad priority task", "2026-08-28", "18:30", "not-a-number"
    ])
    def test_non_numeric_priority_is_rejected(self, mock_input):
        tasks.add_task()
        self.assertEqual(len(tasks.tasks), 0)


class TestCompleteTask(unittest.TestCase):
    def setUp(self):
        tasks.tasks = [{
            "id": 1, "name": "Sample", "date": "2026-08-28",
            "time": "18:30", "priority": 3, "status": "Pending",
        }]

    @patch("builtins.input", return_value="1")
    def test_marks_existing_task_completed(self, mock_input):
        tasks.complete_task()
        self.assertEqual(tasks.tasks[0]["status"], "Completed")

    @patch("builtins.input", return_value="999")
    def test_nonexistent_id_does_not_crash(self, mock_input):
        try:
            tasks.complete_task()
        except Exception as e:  # noqa: BLE001
            self.fail(f"complete_task raised {type(e).__name__}: {e}")
        self.assertEqual(tasks.tasks[0]["status"], "Pending")


class TestDeleteTask(unittest.TestCase):
    def setUp(self):
        tasks.tasks = [{
            "id": 1, "name": "Sample", "date": "2026-08-28",
            "time": "18:30", "priority": 3, "status": "Pending",
        }]

    @patch("builtins.input", return_value="1")
    def test_deletes_existing_task(self, mock_input):
        tasks.delete_task()
        self.assertEqual(len(tasks.tasks), 0)

    @patch("builtins.input", return_value="999")
    def test_nonexistent_id_does_not_crash_or_delete(self, mock_input):
        tasks.delete_task()
        self.assertEqual(len(tasks.tasks), 1)


class TestChangePriority(unittest.TestCase):
    def setUp(self):
        tasks.tasks = [{
            "id": 1, "name": "Sample", "date": "2026-08-28",
            "time": "18:30", "priority": 2, "status": "Pending",
        }]

    @patch("builtins.input", side_effect=["1", "5"])
    def test_changes_priority_of_existing_task(self, mock_input):
        tasks.change_priority()
        self.assertEqual(tasks.tasks[0]["priority"], 5)

    @patch("builtins.input", side_effect=["1", "9"])
    def test_rejects_out_of_range_new_priority(self, mock_input):
        tasks.change_priority()
        # priority should be unchanged since 9 is invalid
        self.assertEqual(tasks.tasks[0]["priority"], 2)


class TestViewTasks(unittest.TestCase):
    def test_empty_list_does_not_crash(self):
        tasks.tasks = []
        try:
            tasks.view_tasks()
        except Exception as e:  # noqa: BLE001
            self.fail(f"view_tasks raised {type(e).__name__}: {e}")

    def test_nonempty_list_does_not_crash(self):
        tasks.tasks = [{
            "id": 1, "name": "Sample", "date": "2026-08-28",
            "time": "18:30", "priority": 3, "status": "Pending",
        }]
        try:
            tasks.view_tasks()
        except Exception as e:  # noqa: BLE001
            self.fail(f"view_tasks raised {type(e).__name__}: {e}")


if __name__ == "__main__":
    unittest.main()
