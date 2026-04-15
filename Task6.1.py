def rank_students_by_average(students):
    """
    Sorts a list of student dictionaries by their average score (descending).

    Expected student format:
    {
        "name": "Hafsat Ahmed Dallatu",
        "scores": [80, 90, 75]
    }
    """

    # Compute average for each student and store it
    for student in students:
        scores = student.get("scores", [])
        student["average"] = sum(scores) / len(scores) if scores else 0

    # Sort by average (highest → lowest)
    ranked_students = sorted(students, key=lambda s: s["average"], reverse=True)

    return ranked_students
