import unittest
from unittest.mock import MagicMock, patch
import tkinter as tk

# Import your module
import Task1.2.py as app  


class TestStudentManager(unittest.TestCase):

    def setUp(self):
        # Create a fake Tk root (does not open a window)
        self.root = tk.Tk()
        self.root.withdraw()

        # Mock backend functions
        app.backend_students.add_student = MagicMock()
        app.backend_students.remove_student = MagicMock()

        # Mock GUI widgets
        app.entry_first_name = tk.Entry(self.root)
        app.entry_last_name = tk.Entry(self.root)
        app.entry_student_id = tk.Entry(self.root)
        app.listbox_students = tk.Listbox(self.root)

    def test_add_student_success(self):
        # Fill entries
        app.entry_first_name.insert(0, "John")
        app.entry_last_name.insert(0, "Doe")
        app.entry_student_id.insert(0, "2025001")

        app.add_student()

        # Check backend call
        app.backend_students.add_student.assert_called_with("John", "Doe", "2025001")

        # Check listbox update
        self.assertEqual(app.listbox_students.get(0), "2025001 - John Doe")

    @patch("tkinter.messagebox.showwarning")
    def test_add_student_missing_fields(self, mock_warning):
        app.add_student()
        mock_warning.assert_called_once()

    def test_remove_student_success(self):
        # Insert a student into listbox
        app.listbox_students.insert(0, "2025001 - John Doe")
        app.listbox_students.selection_set(0)

        app.remove_student()

        # Check backend call
        app.backend_students.remove_student.assert_called_with("2025001")

        # Check listbox is empty
        self.assertEqual(app.listbox_students.size(), 0)

    @patch("tkinter.messagebox.showwarning")
    def test_remove_student_no_selection(self, mock_warning):
        app.remove_student()
        mock_warning.assert_called_once()


if __name__ == "__main__":
    unittest.main()
