"""
Tests for storage.py — save/load persistence.

Uses a separate test file (not the real tasks.txt) so running the
test suite never touches your actual saved tasks.
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import storage

TEST_FILE = "test_tasks_storage.txt"

SAMPLE_TASKS = [
    {
        "id": 1,
        "name": "Complete Python assignment",
        "date": "2026-08-28",
        "time": "18:30",
        "priority": 4,
        "status": "Pending",
    },
    {
        "id": 2,
        "name": "Buy groceries",
        "date": "2026-08-29",
        "time": "10:00",
        "priority": 1,
        "status": "Completed",
    },
]


class TestStorage(unittest.TestCase):
    def tearDown(self):
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    def test_save_then_load_round_trip(self):
        storage.save_tasks(SAMPLE_TASKS, filename=TEST_FILE)
        loaded = storage.load_tasks(filename=TEST_FILE)

        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0]["name"], "Complete Python assignment")
        self.assertEqual(loaded[0]["priority"], 4)
        self.assertEqual(loaded[1]["status"], "Completed")

    def test_save_returns_true_on_success(self):
        result = storage.save_tasks(SAMPLE_TASKS, filename=TEST_FILE)
        self.assertTrue(result)

    def test_load_with_no_file_returns_empty_list(self):
        # first run: file genuinely doesn't exist yet
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)
        result = storage.load_tasks(filename=TEST_FILE)
        self.assertEqual(result, [])

    def test_load_skips_malformed_lines(self):
        with open(TEST_FILE, "w", encoding="utf-8") as f:
            f.write("1|Good task|2026-08-28|18:30|3|Pending\n")
            f.write("this line is broken and missing fields\n")
            f.write("2|Another good task|2026-08-29|09:00|2|Completed\n")

        loaded = storage.load_tasks(filename=TEST_FILE)
        # only the 2 well-formed lines should survive
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0]["name"], "Good task")
        self.assertEqual(loaded[1]["name"], "Another good task")

    def test_load_skips_line_with_invalid_priority(self):
        with open(TEST_FILE, "w", encoding="utf-8") as f:
            f.write("1|Task with bad priority|2026-08-28|18:30|not-a-number|Pending\n")
            f.write("2|Valid task|2026-08-29|09:00|2|Completed\n")

        loaded = storage.load_tasks(filename=TEST_FILE)
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0]["name"], "Valid task")

    def test_load_skips_blank_lines(self):
        with open(TEST_FILE, "w", encoding="utf-8") as f:
            f.write("1|Task one|2026-08-28|18:30|3|Pending\n")
            f.write("\n")
            f.write("2|Task two|2026-08-29|09:00|2|Completed\n")

        loaded = storage.load_tasks(filename=TEST_FILE)
        self.assertEqual(len(loaded), 2)


if __name__ == "__main__":
    unittest.main()
