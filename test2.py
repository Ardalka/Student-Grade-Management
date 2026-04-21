import unittest
from unittest.mock import MagicMock
import tkinter as tk
from tkinter import ttk

import Feature2 as app  


class TestLoadTable(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()

        # Mock tree widget
        app.tree = ttk.Treeview(self.root, columns=("Student", "Course", "Grade"))
        app.tree.insert = MagicMock()
        app.tree.get_children = MagicMock(return_value=["row1", "row2"])
        app.tree.delete = MagicMock()

        # Mock grades dictionary
        app.grades = {
            ("Alice", "Math"): 85,
            ("Bob", "Science"): 90
        }

    def test_load_table_clears_existing_rows(self):
        app.load_table()
        app.tree.delete.assert_any_call("row1")
        app.tree.delete.assert_any_call("row2")

    def test_load_table_inserts_new_rows(self):
        app.load_table()
        app.tree.insert.assert_any_call("", "end", values=("Alice", "Math", 85))
        app.tree.insert.assert_any_call("", "end", values=("Bob", "Science", 90))


if __name__ == "__main__":
    unittest.main()
