import sqlite3
# This function adds a new student to the database
def add_student(first_name, last_name, student_id):
    connection = sqlite3.connect("student_management.db")
    cursor = connection.cursor()
    
    try:
        # INSERT operation to add data
        cursor.execute('''
            INSERT INTO students (first_name, last_name, student_id)
            VALUES (?, ?, ?)
        ''', (first_name, last_name, student_id))
        
        connection.commit()
        print(f"Success: Student {first_name} {last_name} (ID: {student_id}) has been added.")
        
    except sqlite3.IntegrityError:
        # This error happens if we try to add a student_id that already exists
        print(f"Error: A student with ID {student_id} already exists!")
        
    finally:
        connection.close()

# This function removes a student from the database using their student_id
def remove_student(student_id):
    """Removes a student from the database using their student_id."""
    connection = sqlite3.connect("student_management.db")
    cursor = connection.cursor()
    
    # First, check if the student exists
    cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
    if cursor.fetchone() is None:
        print(f"Error: Student with ID {student_id} not found.")
    else:
        # DELETE operation to remove data
        cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
        connection.commit()
        print(f"Success: Student with ID {student_id} has been removed.")
        
    connection.close()

# --- TESTING THE FUNCTIONS ---
add_student("Arda", "Ilktug", "2025001")
add_student("Paa Kofi", "Nyarkoh", "2025002")

# --- TESTING THE REMOVE FUNCTION ---
# remove_student("2025001")