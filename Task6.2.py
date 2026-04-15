import sqlite3
import tkinter as tk

def get_course_average(db_connection, course_id):
    query = """
        SELECT AVG(score) AS class_average
        FROM grades
        WHERE course_id = ?;
    """
    cursor = db_connection.cursor()
    cursor.execute(query, (course_id,))
    result = cursor.fetchone()
    return result[0] if result[0] is not None else 0

def show_course_average():
    course_id = course_id_entry.get()
    avg = get_course_average(db, course_id)
    average_label.config(text=f"Class Average: {avg:.2f}")

# GUI Setup
db = sqlite3.connect("student_management.db")

root = tk.Tk()
root.title("Course Average Calculator")

tk.Label(root, text="Enter Course ID:").pack(pady=5)
course_id_entry = tk.Entry(root)
course_id_entry.pack(pady=5)

average_label = tk.Label(root, text="Class Average: ")
average_label.pack(pady=10)

tk.Button(root, text="Calculate Average", command=show_course_average).pack(pady=10)

root.mainloop()
