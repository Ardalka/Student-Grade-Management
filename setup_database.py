import sqlite3

# 1. Connect to the database (creates the file if it doesn't exist)
connection = sqlite3.connect("student_management.db")

# 2. Create a cursor object to execute SQL commands
cursor = connection.cursor()

# 3. Create the students table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    student_id TEXT UNIQUE NOT NULL
)
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT NOT NULL,
        course_code TEXT NOT NULL,
        grade_value REAL,
        FOREIGN KEY (student_id) REFERENCES students (student_id),
        FOREIGN KEY (course_code) REFERENCES courses (course_code),
        UNIQUE(student_id, course_code) -- Bir öğrencinin bir derste tek bir notu olur
    )
    ''')

# 4. Commit the changes and close the connection
connection.commit()
connection.close()

print("Success: Database and 'students' table created successfully!")