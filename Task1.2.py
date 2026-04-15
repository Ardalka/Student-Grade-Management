import tkinter as tk
from tkinter import messagebox
import backend_students  # Importing the backend database functions

# --- Functions ---
def add_student():
    # Get user inputs
    f_name = entry_first_name.get().strip()
    l_name = entry_last_name.get().strip()
    s_id = entry_student_id.get().strip()

    # Check if any field is empty
    if f_name == "" or l_name == "" or s_id == "":
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return

    # 1. ADD TO DATABASE (Calls the backend function)
    backend_students.add_student(f_name, l_name, s_id)

    # 2. ADD TO GUI LISTBOX
    display_text = f"{s_id} - {f_name} {l_name}"
    listbox_students.insert(tk.END, display_text)

    # Clear the entry boxes after adding
    entry_first_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    entry_student_id.delete(0, tk.END)


def remove_student():
    selected_index = listbox_students.curselection()
    
    if not selected_index:
        messagebox.showwarning("Selection Error", "Please select a student to remove.")
        return

    # Get the selected text from Listbox (e.g., "2025001 - John Doe")
    selected_text = listbox_students.get(selected_index)
    
    # Split the text by " - " and get the first part (which is the student_id)
    student_id = selected_text.split(" - ")[0]

    # 1. REMOVE FROM DATABASE (Calls the backend function)
    backend_students.remove_student(student_id)

    # 2. REMOVE FROM GUI LISTBOX
    listbox_students.delete(selected_index)


# --- Main Window ---
root = tk.Tk()
root.title("Student Manager")
root.geometry("400x450") # Expanded the window slightly to fit new fields

# --- Widgets ---
tk.Label(root, text="Student ID:").pack(pady=2)
entry_student_id = tk.Entry(root, width=30)
entry_student_id.pack(pady=2)

tk.Label(root, text="First Name:").pack(pady=2)
entry_first_name = tk.Entry(root, width=30)
entry_first_name.pack(pady=2)

tk.Label(root, text="Last Name:").pack(pady=2)
entry_last_name = tk.Entry(root, width=30)
entry_last_name.pack(pady=2)

btn_add = tk.Button(root, text="Add Student", width=20, command=add_student)
btn_add.pack(pady=10)

btn_remove = tk.Button(root, text="Remove Student", width=20, command=remove_student)
btn_remove.pack(pady=5)

listbox_students = tk.Listbox(root, width=50, height=10)
listbox_students.pack(pady=10)

# --- Run App ---
root.mainloop()