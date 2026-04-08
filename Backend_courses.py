import sqlite3
#Add funciton
def add_course(course_code, course_name):
    """Adds a new course to the database."""
    connection = sqlite3.connect("student_management.db")
    cursor = connection.cursor()

    cursor.execute('''
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_code TEXT UNIQUE NOT NULL,
    course_name TEXT NOT NULL
)
''')
    try:
        cursor.execute('''
            INSERT INTO courses (course_code, course_name)
            VALUES (?, ?)
        ''', (course_code, course_name))
        
        connection.commit()
        print(f"Success: Course '{course_name}' (Code: {course_code}) has been added.")
        
    except sqlite3.IntegrityError:
        # Prevents adding the same course code twice
        print(f"Error: A course with code '{course_code}' already exists!")
        
    finally:
        connection.close()

#Remove function
def remove_course(course_code):
    """Removes a course from the database using its course_code."""
    connection = sqlite3.connect("student_management.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM courses WHERE course_code = ?", (course_code,))
    if cursor.fetchone() is None:
        print(f"Error: Course with code '{course_code}' not found.")
    else:
        cursor.execute("DELETE FROM courses WHERE course_code = ?", (course_code,))
        connection.commit()
        print(f"Success: Course with code '{course_code}' has been removed.")
        
    connection.close()
