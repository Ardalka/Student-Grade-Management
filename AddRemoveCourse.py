import tkinter as tk
from tkinter import messagebox
from backend_students import add_course, remove_course 
courses = []

def add_course():
    course = entry.get()

    if course != "":
        add_course(course_code, course_name)
        listbox.insert(tk.END, course)
        entry.delete(0, tk.END)

def remove_course():
    selected = listbox.curselection()

    if selected:
        course_name = listbox.get(index)
        remove_course(course_code)
        listbox.delete(index)

root = tk.Tk()
root.title("Course Management")

label = tk.Label(root, text="Course Management")
label.pack()

entry = tk.Entry(root, width=30)
entry.pack()

add_btn = tk.Button(root, text="Add Course", command=add_course)
add_btn.pack()

remove_btn = tk.Button(root, text="Remove Course", command=remove_course)
remove_btn.pack()

listbox = tk.Listbox(root, width=40)
listbox.pack()

root.mainloop()
