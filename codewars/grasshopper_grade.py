def get_grade(s1, s2, s3):
    grade = ""
    avg_score = (s1 + s2 + s3) / 3
    if avg_score >= 90:
        grade = "A"
    elif avg_score >= 80:
        grade = "B"
    elif avg_score >= 70:
        grade = "C"
    elif avg_score >= 60:
        grade = "D"
    else:
        grade = "F"

    return grade
