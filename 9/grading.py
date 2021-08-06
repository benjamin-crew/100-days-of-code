student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for student, score in student_scores.items():
    if score >= 91:
        student_grades[student] = "Outstanding"
    elif score >= 81 and score < 91:
        student_grades[student] = "Exceeds expectations"
    elif score >= 71 and score < 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

   

print(student_grades)