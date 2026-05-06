import unittest
import sqlite3
from Backend_courses.py import add_course, remove_course

class TestCourseManagement(unittest.TestCase):

    def setUp(self):
        # Create an in-memory DB for testing
        self.connection = sqlite3.connect(":memory:")
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_code TEXT UNIQUE NOT NULL,
                course_name TEXT NOT NULL
            )
        """)
        self.connection.commit()

        # Patch sqlite3.connect to use in-memory DB
        self.original_connect = sqlite3.connect
        sqlite3.connect = lambda _: self.connection

    def tearDown(self):
        sqlite3.connect = self.original_connect
        self.connection.close()

    # -------------------------
    # Input–Output Tests
    # -------------------------
    def test_add_course_success(self):
        result = add_course("CS101", "Intro to CS")
        self.assertTrue(result)

    def test_remove_course_success(self):
        add_course("CS102", "Data Structures")
        result = remove_course("CS102")
        self.assertTrue(result)

    # -------------------------
    # Edge Cases
    # -------------------------
    def test_add_duplicate_course(self):
        add_course("CS103", "Algorithms")
        result = add_course("CS103", "Algorithms")
        self.assertFalse(result)

    def test_remove_nonexistent_course(self):
        result = remove_course("NONEXIST")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
