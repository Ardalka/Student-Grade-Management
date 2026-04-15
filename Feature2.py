import tkinter as tk
from tkinter import ttk, messagebox

students = ["Alice", "Bob", "Charlie", "Diana"]
courses = ["Math", "Science", "English", "History"]

# (student, course) -> score
grades = {}

# ---------------------------
# Core Functions
# ---------------------------
def save_grade():
    student = student_var.get()
    course = course_var.get()
    score = score_var.get()

    if not student or not course or not score:
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        score_value = float(score)
    except ValueError:
        messagebox.showerror("Error", "Score must be a number!")
        return

    key = (student, course)
    action = "Updated" if key in grades else "Recorded"

    grades[key] = score_value

    messagebox.showinfo("Success", f"{action} grade for {student} in {course}")
    refresh_display()


def load_grade(event=None):
    student = student_var.get()
    course = course_var.get()
    key = (student, course)

    if key in grades:
        score_var.set(str(grades[key]))
    else:
        score_var.set("")


def refresh_display():
    listbox.delete(0, tk.END)
    for (student, course), score in grades.items():
        listbox.insert(tk.END, f"{student} - {course}: {score}")


# ---------------------------
# GUI Setup
# ---------------------------
root = tk.Tk()
root.title("Student Grade Manager")
root.geometry("500x400")

# Variables
student_var = tk.StringVar()
course_var = tk.StringVar()
score_var = tk.StringVar()

# ---------------------------
# Form UI
# ---------------------------
tk.Label(root, text="Select Student").pack(pady=5)
student_cb = ttk.Combobox(root, textvariable=student_var, values=students, state="readonly")
student_cb.pack()

tk.Label(root, text="Select Course").pack(pady=5)
course_cb = ttk.Combobox(root, textvariable=course_var, values=courses, state="readonly")
course_cb.pack()

tk.Label(root, text="Enter Score").pack(pady=5)
score_entry = tk.Entry(root, textvariable=score_var)
score_entry.pack()

# Bind selection change to auto-load grade
student_cb.bind("<<ComboboxSelected>>", load_grade)
course_cb.bind("<<ComboboxSelected>>", load_grade)

# Buttons
tk.Button(root, text="Save / Update Grade", command=save_grade, bg="green", fg="white").pack(pady=10)

# Display area
tk.Label(root, text="Recorded Grades").pack(pady=5)
listbox = tk.Listbox(root, width=50)
listbox.pack()

# Initial load
refresh_display()

# Run app
root.mainloop()