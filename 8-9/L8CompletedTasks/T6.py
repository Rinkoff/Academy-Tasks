student_grades = {
    "Ivan" : [5, 6, 4, 5],
    "Peter": [6, 6, 6, 6],
    "Maria": [4, 5, 3, 4],
    "Anna": [6, 5, 6, 4]
}

for student,grades in student_grades.items():
    print(student, sum(grades)/len(grades))

