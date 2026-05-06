import unittest
import os
import csv
from unittest.mock import patch

# import your function (adjust filename if needed)
from frontend import save_to_file


class FakeTree:
    def __init__(self):
        self.data = [
            ("Alice", "Math", "A"),
            ("Bob", "Science", "B")
        ]

    def get_children(self):
        return range(len(self.data))

    def item(self, row):
        return {"values": self.data[row]}


class TestSaveToFile(unittest.TestCase):

    @patch("tkinter.messagebox.showinfo")  # prevent popup during test
    def test_csv_creation(self, mock_msg):
        tree = FakeTree()

        # run function
        save_to_file(tree)

        # check file exists
        self.assertTrue(os.path.exists("grades_export.csv"))

        # check content
        with open("grades_export.csv", newline="") as f:
            reader = list(csv.reader(f))

        self.assertEqual(reader[0], ["Student", "Course", "Grade"])
        self.assertEqual(reader[1], ["Alice", "Math", "A"])
        self.assertEqual(reader[2], ["Bob", "Science", "B"])

        # check messagebox called
        mock_msg.assert_called_once()

        # cleanup
        os.remove("grades_export.csv")


if __name__ == "__main__":
    unittest.main()