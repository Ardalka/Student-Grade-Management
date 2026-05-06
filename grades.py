def grades_to_gpa(avg_score: float):

    if avg_score < 0 or avg_score > 100:
        return None

    if avg_score < 50:
        return 0.0
    elif avg_score < 60:
        return 1.0
    elif avg_score < 70:
        return 2.0
    elif avg_score < 80:
        return 3.0
    elif avg_score < 90:
        return 4.0
    else:
        return 5.0