import unittest
from unittest.mock import patch
import tkinter as tk

import feature3 as app  


class TestGradeManager(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()

        # Reset grades dictionary
        app.grades = {}

        # Mock GUI variables
        app.student_var = tk.StringVar()
        app.course_var = tk.StringVar()
        app.score_var = tk.StringVar()

        # Mock listbox
        app.listbox = tk.Listbox(self.root)

    @patch("tkinter.messagebox.showinfo")
    def test_save_grade_new(self, mock_info):
        app.student_var.set("Alice")
        app.course_var.set("Math")
        app.score_var.set("90")

        app.save_grade()

        self.assertEqual(app.grades[("Alice", "Math")], 90.0)
        mock_info.assert_called_once()

    @patch("tkinter.messagebox.showerror")
    def test_save_grade_invalid_score(self, mock_error):
        app.student_var.set("Alice")
        app.course_var.set("Math")
        app.score_var.set("abc")

        app.save_grade()
        mock_error.assert_called_once()

    def test_load_grade_existing(self):
        app.grades[("Bob", "Science")] = 88
        app.student_var.set("Bob")
        app.course_var.set("Science")

        app.load_grade()
        self.assertEqual(app.score_var.get(), "88")

    def test_refresh_display(self):
        app.grades = {("Alice", "Math"): 95}
        app.refresh_display()

        self.assertEqual(app.listbox.get(0), "Alice - Math: 95")


if __name__ == "__main__":
    unittest.main()
