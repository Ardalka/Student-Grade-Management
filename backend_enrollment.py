import sqlite3

def enroll_student(student_id, course_code):
    """Registers a student to a course."""
    connection = sqlite3.connect("student_management.db")
    cursor = connection.cursor()
    
    try:
        cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
        if cursor.fetchone() is None:
            print(f"Error: Student {student_id} does not exist in the system.")
            return
        cursor.execute("SELECT * FROM courses WHERE course_code = ?", (course_code,))
        if cursor.fetchone() is None:
            print(f"Error: Course {course_code} does not exist in the system.")
            return

        cursor.execute('''
            INSERT INTO grades (student_id, course_code, grade_value)
            VALUES (?, ?, NULL)
        ''', (student_id, course_code))
        connection.commit()
        print(f"Success: Student {student_id} has been enrolled in {course_code}.")
        
    except sqlite3.IntegrityError:
        print(f"Error: Student {student_id} is already enrolled in {course_code}.")
        
    finally:
        connection.close()


def update_grade(student_id, course_code, grade):
    """Updates the grade for an enrolled student."""
    connection = sqlite3.connect("student_management.db")
    cursor = connection.cursor()
    
    cursor.execute('''
        SELECT * FROM grades WHERE student_id = ? AND course_code = ?
    ''', (student_id, course_code))
    
    if cursor.fetchone() is None:
        print(f"Error: Student {student_id} is not enrolled in {course_code}. Enroll them first.")
    else:
        cursor.execute('''
            UPDATE grades SET grade_value = ? 
            WHERE student_id = ? AND course_code = ?
        ''', (grade, student_id, course_code))
        connection.commit()
        print(f"Success: Grade for {student_id} in {course_code} updated to {grade}.")
        
    connection.close()


def get_student_report(student_id):
    """Generates a transcript linking student details, courses, and grades."""
    connection = sqlite3.connect("student_management.db")
    cursor = connection.cursor()
    
    # Advanced SQL JOIN: Connecting 3 tables to get a full report
    query = '''
    SELECT students.first_name, students.last_name, courses.course_name, grades.grade_value
    FROM grades
    JOIN students ON grades.student_id = students.student_id
    JOIN courses ON grades.course_code = courses.course_code
    WHERE grades.student_id = ?
    '''
    
    cursor.execute(query, (student_id,))
    results = cursor.fetchall()
    
    if not results:
        print(f"No enrollment records found for Student ID: {student_id}")
    else:
        print(f"\n--- Transcript for {results[0][0]} {results[0][1]} (ID: {student_id}) ---")
        for row in results:
            course_name = row[2]
            grade = row[3] if row[3] is not None else "Not Graded Yet"
            print(f"Course: {course_name} | Grade: {grade}")
        print("--------------------------------------------------\n")
        
    connection.close()

# --- TESTING THE FUNCTIONS ---
# enroll_student("2025001", "CS101")
# update_grade("2025001", "CS101", 95.5)
# get_student_report("2025001")