import unittest
import sqlite3
from Task6.2.py import get_course_average

class TestCourseAverage(unittest.TestCase):

    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE grades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER,
                course_id TEXT,
                score REAL
            )
        """)
        self.connection.commit()

    def tearDown(self):
        self.connection.close()

    # -------------------------
    # Input–Output Tests
    # -------------------------
    def test_average_single_student(self):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO grades (course_id, score) VALUES (?, ?)", ("CS101", 90))
        self.connection.commit()

        avg = get_course_average(self.connection, "CS101")
        self.assertEqual(avg, 90)

    def test_average_multiple_students(self):
        cursor = self.connection.cursor()
        cursor.executemany(
            "INSERT INTO grades (course_id, score) VALUES (?, ?)",
            [("CS101", 80), ("CS101", 100), ("CS101", 90)]
        )
        self.connection.commit()

        avg = get_course_average(self.connection, "CS101")
        self.assertEqual(avg, 90)

    # -------------------------
    # Edge Cases
    # -------------------------
    def test_no_grades(self):
        avg = get_course_average(self.connection, "EMPTY101")
        self.assertEqual(avg, 0)

    def test_nonexistent_course(self):
        avg = get_course_average(self.connection, "DOESNOTEXIST")
        self.assertEqual(avg, 0)

if __name__ == "__main__":
    unittest.main()
