def add_student(student, students):
    student = student.capitalize()
    students.append(student)

def remove_student(student,students):
    student = student.capitalize()
    students.remove(student)

def show_students(students):
    print(students)
