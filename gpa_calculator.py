GPA_SCALE = {
    "A+": 4.3,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D": 1.0,
    "F": 0.0
}

def grade_to_gpa(grade):
    return GPA_SCALE.get(grade.upper(), 0.0)

def calculate_weighted_gpa(courses):
    total_credits = 0
    total_points = 0
    for course in courses:
        credit = course["credit"]
        grade = course["grade"]
        gpa = grade_to_gpa(grade)
        total_credits += credit
        total_points += credit * gpa
    if total_credits == 0:
        return 0.0
    return total_points / total_credits