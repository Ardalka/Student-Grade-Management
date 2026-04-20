import unittest
import sqlite3

# Kendi dosya adından import ettiğini varsayıyorum.
from backend_students import add_student, remove_student

class TestStudentFeatures(unittest.TestCase):

    def setUp(self):
        conn = sqlite3.connect("student_management.db")
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            first_name TEXT NOT NULL,
                            last_name TEXT NOT NULL,
                            student_id TEXT UNIQUE NOT NULL)''')
        cursor.execute("DELETE FROM students")
        conn.commit()
        conn.close()

    def check_student_in_db(self, student_id):
        conn = sqlite3.connect("student_management.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
        result = cursor.fetchone()
        conn.close()
        return result is not None

    # FEATURE: add_student Testleri

    # Input-Output Test Cases 
    def test_add_TC1(self):
        add_student("Arda", "Ilktug", "2025001")
        self.assertTrue(self.check_student_in_db("2025001"))

    def test_add_TC2(self):
        add_student("Paa Kofi", "Nyarkoh", "2025002")
        self.assertTrue(self.check_student_in_db("2025002"))

    def test_add_TC3(self):
        add_student("Hafsat Ahmed", "Dallatu", "2025003")
        self.assertTrue(self.check_student_in_db("2025003"))

    def test_add_TC4(self):
        add_student("Arda", "Ilktug", "special_ID_2026")
        self.assertTrue(self.check_student_in_db("special_ID_2026"))

    # --- Edge Cases ---
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
        add_student("John", "Doe", "2025001")
        add_student("Jane", "Smith", "2025001")
        conn = sqlite3.connect("student_management.db")
        cursor = conn.cursor()
        cursor.execute("SELECT first_name FROM students WHERE student_id = '2025001'")
        name = cursor.fetchone()[0]
        conn.close()
        
        self.assertEqual(name, "John")

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

    # FEATURE: remove_student Tests
    
    # Input-Output Test Cases 
    def test_remove_TC1(self):
        add_student("Arda", "Ilktug", "2025001")
        remove_student("2025001")
        self.assertFalse(self.check_student_in_db("2025001"))

    def test_remove_TC2(self):
        add_student("Arda", "Ilktug", "special_ID_2026")
        remove_student("special_ID_2026")
        self.assertFalse(self.check_student_in_db("special_ID_2026"))

    # Edge Cases
    def test_remove_EC1_strip_spaces(self):
        add_student("Test", "Student", "2025001")
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


if __name__ == '__main__':
    unittest.main()