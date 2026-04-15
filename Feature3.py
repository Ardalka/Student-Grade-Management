import tkinter as tk
from tkinter import ttk, messagebox

students = ["Alice", "Bob", "Charlie", "Diana"]
courses = ["Math", "Science", "English", "History"]

grades = {
    ("Alice", "Math"): 85,
    ("Alice", "Science"): 90,
    ("Bob", "Math"): 72,
    ("Charlie", "English"): 88
}

# ---------------------------
# Function: Load table data
# ---------------------------
def load_table():
    # Clear existing rows
    for row in tree.get_children():
        tree.delete(row)

    # Insert all grades
    for (student, course), score in grades.items():
        tree.insert("", "end", values=(student, course, score))


# ---------------------------
# GUI Setup
# ---------------------------
root = tk.Tk()
root.title("Student Grades Table View")
root.geometry("600x400")

# ---------------------------
# Table (Treeview)
# ---------------------------
columns = ("Student", "Course", "Grade")

tree = ttk.Treeview(root, columns=columns, show="headings")

# Define headings
tree.heading("Student", text="Student")
tree.heading("Course", text="Course")
tree.heading("Grade", text="Grade")

# Column width
tree.column("Student", width=150)
tree.column("Course", width=150)
tree.column("Grade", width=100)

tree.pack(fill="both", expand=True, pady=20)

# ---------------------------
# Button to Refresh Table
# ---------------------------
tk.Button(root, text="Show All Grades", command=load_table).pack()

# Initial load
load_table()

# Run app
root.mainloop()