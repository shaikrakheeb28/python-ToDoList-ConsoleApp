# test_to_do_list.py

import unittest
from to_do_list import ToDoList

class TestToDoList(unittest.TestCase):
    def setUp(self):
        self.todo = ToDoList()

    def test_add_task(self):
        self.todo.add_task("Test Task")
        self.assertEqual(len(self.todo.tasks), 1)
        self.assertEqual(self.todo.tasks[0]["task"], "Test Task")

    def test_mark_done(self):
        self.todo.add_task("Task to be done")
        self.todo.mark_done(0)
        self.assertTrue(self.todo.tasks[0]["done"])

    def test_delete_task(self):
        self.todo.add_task("Task to delete")
        self.todo.delete_task(0)
        self.assertEqual(len(self.todo.tasks), 0)

if __name__ == "__main__":
    unittest.main()
