import sqlite3

def add_or_update_grade(student_id, course_code, grade):
    """Adds a new grade or updates an existing one."""
    connection = sqlite3.connect("student_management.db")
    cursor = connection.cursor()
    
    try:
        cursor.execute('''
            INSERT OR REPLACE INTO grades (student_id, course_code, grade_value)
            VALUES (?, ?, ?)
        ''', (student_id, course_code, grade))
        connection.commit()
        print(f"Success: Grade {grade} assigned to {student_id} for {course_code}.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()

def delete_grade(student_id, course_code):
    """Removes a grade record from the database."""
    connection = sqlite3.connect("student_management.db")
    cursor = connection.cursor()
    cursor.execute('''
        DELETE FROM grades WHERE student_id = ? AND course_code = ?
    ''', (student_id, course_code))
    if cursor.rowcount > 0:
        connection.commit()
        print(f"Success: Grade for {student_id} in {course_code} deleted.")
    else:
        print("Error: Record not found.")
    connection.close()