import unittest

from src.task_parser import Task, parse_task


class ParseTaskTests(unittest.TestCase):
    def test_parses_open_task(self):
        self.assertEqual(parse_task("- [ ] Write documentation"), Task("Write documentation"))

    def test_parses_completed_task(self):
        self.assertEqual(parse_task("- [x] Ship feature"), Task("Ship feature", completed=True))

    def test_ignores_ordinary_text(self):
        self.assertIsNone(parse_task("not a task"))


if __name__ == "__main__":
    unittest.main()
