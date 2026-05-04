import unittest
import sqlite3

from backend_students import add_student, remove_student
from backhend_grades import add_or_update_grade, delete_grade


class TestStudentFeatures(unittest.TestCase):

    def setUp(self):
        conn = sqlite3.connect("student_management.db")
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            first_name TEXT NOT NULL,
                            last_name TEXT NOT NULL,
                            student_id TEXT UNIQUE NOT NULL)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS grades (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            student_id TEXT NOT NULL,
                            course_code TEXT NOT NULL,
                            grade_value REAL,
                            UNIQUE(student_id, course_code))''')
        cursor.execute("DELETE FROM grades")
        cursor.execute("DELETE FROM students")
        cursor.execute("INSERT INTO students (first_name, last_name, student_id) VALUES (?, ?, ?)",
                       ("Arda", "Ilktug", "2025001"))
        cursor.execute("INSERT INTO students (first_name, last_name, student_id) VALUES (?, ?, ?)",
                       ("Paa Kofi", "Nyarkoh", "2025002"))
        conn.commit()
        conn.close()

    def check_student_in_db(self, student_id):
        conn = sqlite3.connect("student_management.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
        result = cursor.fetchone()
        conn.close()
        return result is not None

    def get_grade_from_db(self, student_id, course_code):
        conn = sqlite3.connect("student_management.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT grade_value FROM grades WHERE student_id = ? AND course_code = ?",
            (student_id, course_code)
        )
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None

    def grade_exists(self, student_id, course_code):
        conn = sqlite3.connect("student_management.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id FROM grades WHERE student_id = ? AND course_code = ?",
            (student_id, course_code)
        )
        result = cursor.fetchone()
        conn.close()
        return result is not None

    # ================================================================== #
    # FEATURE 1: add_student
    # ================================================================== #

    # Input-Output Test Cases
    def test_add_TC1(self):
        add_student("Hafsat Ahmed", "Dallatu", "2025003")
        self.assertTrue(self.check_student_in_db("2025003"))

    def test_add_TC2(self):
        add_student("Paa Kofi", "Nyarkoh", "2025010")
        self.assertTrue(self.check_student_in_db("2025010"))

    def test_add_TC3(self):
        add_student("Arda", "Ilktug", "special_ID_2026")
        self.assertTrue(self.check_student_in_db("special_ID_2026"))

    def test_add_TC4(self):
        add_student("Antu", "Student", "2025011")
        self.assertTrue(self.check_student_in_db("2025011"))

    # Edge Cases
    def test_add_EC1(self):
        add_student("A", "B", "1")
        self.assertTrue(self.check_student_in_db("1"))

    def test_add_EC2(self):
        add_student("Ahmet", "Yilmaz", "999999")
        self.assertTrue(self.check_student_in_db("999999"))

    def test_add_EC3(self):
        add_student("Antu", "Student", "2025-X-Admin")
        self.assertTrue(self.check_student_in_db("2025-X-Admin"))

    # Error Handling Tests
    def test_add_EH1_duplicate_id(self):
        add_student("Jane", "Smith", "2025001")  # 2025001 zaten setUp'ta eklendi
        conn = sqlite3.connect("student_management.db")
        cursor = conn.cursor()
        cursor.execute("SELECT first_name FROM students WHERE student_id = '2025001'")
        name = cursor.fetchone()[0]
        conn.close()
        self.assertEqual(name, "Arda")  # İlk kayıt korunmalı

    def test_add_EH2_null_first_name(self):
        try:
            add_student(None, "Smith", "2025004")
        except Exception:
            pass
        self.assertFalse(self.check_student_in_db("2025004"))

    def test_add_EH3_null_last_name(self):
        try:
            add_student("James", None, "2025005")
        except Exception:
            pass
        self.assertFalse(self.check_student_in_db("2025005"))

    # ================================================================== #
    # FEATURE 2: remove_student
    # ================================================================== #

    # Input-Output Test Cases
    def test_remove_TC1(self):
        remove_student("2025001")
        self.assertFalse(self.check_student_in_db("2025001"))

    def test_remove_TC2(self):
        add_student("Arda", "Ilktug", "special_ID_2026")
        remove_student("special_ID_2026")
        self.assertFalse(self.check_student_in_db("special_ID_2026"))

    # Edge Cases
    def test_remove_EC1_strip_spaces(self):
        remove_student(" 2025001 ")
        self.assertFalse(self.check_student_in_db("2025001"))

    def test_remove_EC2_minimal_length(self):
        add_student("A", "B", "1")
        remove_student("1")
        self.assertFalse(self.check_student_in_db("1"))

    def test_remove_EC3_special_chars(self):
        add_student("Antu", "Student", "2025-X-Admin")
        remove_student("2025-X-Admin")
        self.assertFalse(self.check_student_in_db("2025-X-Admin"))

    # Error Handling Tests
    def test_remove_EH1_id_not_found(self):
        try:
            remove_student("0000000")
            crashed = False
        except Exception:
            crashed = True
        self.assertFalse(crashed)

    def test_remove_EH2_none_input(self):
        try:
            remove_student(None)
            crashed = False
        except Exception:
            crashed = True
        self.assertFalse(crashed)

    def test_remove_EH3_invalid_id(self):
        try:
            remove_student("Arda")
            crashed = False
        except Exception:
            crashed = True
        self.assertFalse(crashed)

    # ================================================================== #
    # FEATURE 3: add_or_update_grade
    # ================================================================== #

    # Input-Output Test Cases
    def test_add_grade_TC1(self):
        add_or_update_grade("2025001", "CS101", 85.0)
        self.assertEqual(self.get_grade_from_db("2025001", "CS101"), 85.0)

    def test_add_grade_TC2(self):
        add_or_update_grade("2025002", "MATH201", 90.5)
        self.assertEqual(self.get_grade_from_db("2025002", "MATH201"), 90.5)

    def test_add_grade_TC3(self):
        add_or_update_grade("2025001", "CS101", 70.0)
        add_or_update_grade("2025001", "MATH201", 80.0)
        self.assertEqual(self.get_grade_from_db("2025001", "CS101"), 70.0)
        self.assertEqual(self.get_grade_from_db("2025001", "MATH201"), 80.0)

    # Edge Cases
    def test_add_grade_EC1_zero_grade(self):
        add_or_update_grade("2025001", "CS101", 0.0)
        self.assertEqual(self.get_grade_from_db("2025001", "CS101"), 0.0)

    def test_add_grade_EC2_max_grade(self):
        add_or_update_grade("2025001", "CS101", 100.0)
        self.assertEqual(self.get_grade_from_db("2025001", "CS101"), 100.0)

    def test_add_grade_EC3_special_course_code(self):
        add_or_update_grade("2025001", "CS-101_ADV", 75.0)
        self.assertEqual(self.get_grade_from_db("2025001", "CS-101_ADV"), 75.0)

    # Error Handling Tests
    def test_add_grade_EH1_update_existing(self):
        add_or_update_grade("2025001", "CS101", 60.0)
        add_or_update_grade("2025001", "CS101", 95.0)
        self.assertEqual(self.get_grade_from_db("2025001", "CS101"), 95.0)

    def test_add_grade_EH2_none_grade(self):
        try:
            add_or_update_grade("2025001", "CS101", None)
            crashed = False
        except Exception:
            crashed = True
        self.assertFalse(crashed)

    def test_add_grade_EH3_none_student_id(self):
        try:
            add_or_update_grade(None, "CS101", 80.0)
            crashed = False
        except Exception:
            crashed = True
        self.assertFalse(crashed)

    # ================================================================== #
    # FEATURE 4: delete_grade
    # ================================================================== #

    # Input-Output Test Cases
    def test_delete_grade_TC1(self):
        add_or_update_grade("2025001", "CS101", 85.0)
        delete_grade("2025001", "CS101")
        self.assertFalse(self.grade_exists("2025001", "CS101"))

    def test_delete_grade_TC2(self):
        add_or_update_grade("2025002", "MATH201", 90.0)
        delete_grade("2025002", "MATH201")
        self.assertFalse(self.grade_exists("2025002", "MATH201"))

    def test_delete_grade_TC3(self):
        add_or_update_grade("2025001", "CS101", 70.0)
        add_or_update_grade("2025001", "MATH201", 80.0)
        delete_grade("2025001", "CS101")
        self.assertFalse(self.grade_exists("2025001", "CS101"))
        self.assertTrue(self.grade_exists("2025001", "MATH201"))

    # Edge Cases
    def test_delete_grade_EC1_special_course_code(self):
        add_or_update_grade("2025001", "CS-101_ADV", 75.0)
        delete_grade("2025001", "CS-101_ADV")
        self.assertFalse(self.grade_exists("2025001", "CS-101_ADV"))

    def test_delete_grade_EC2_minimal_ids(self):
        add_or_update_grade("1", "A", 50.0)
        delete_grade("1", "A")
        self.assertFalse(self.grade_exists("1", "A"))

    # Error Handling Tests
    def test_delete_grade_EH1_not_found(self):
        try:
            delete_grade("9999999", "CS101")
            crashed = False
        except Exception:
            crashed = True
        self.assertFalse(crashed)

    def test_delete_grade_EH2_none_student_id(self):
        try:
            delete_grade(None, "CS101")
            crashed = False
        except Exception:
            crashed = True
        self.assertFalse(crashed)

    def test_delete_grade_EH3_none_course_code(self):
        try:
            delete_grade("2025001", None)
            crashed = False
        except Exception:
            crashed = True
        self.assertFalse(crashed)


if __name__ == '__main__':
    unittest.main()