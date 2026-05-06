import csv
from tkinter import messagebox

def save_to_file(tree):
    with open("grades_export.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Student", "Course", "Grade"])

        for row in tree.get_children():
            writer.writerow(tree.item(row)["values"])

    messagebox.showinfo("Success", "Grades saved to file!")