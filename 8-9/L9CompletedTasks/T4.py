employees = [
    ("Ivan", 2500, "IT"),
    ("Maria", 3000, "HR"),
    ("Peter", 2800, "IT"),
    ("Anna", 3200, "Sales"),
    ("George", 3500, "IT")
]

department = input("Enter a department:")
employees_in_department = []

for employee in employees:
    if employee[2] == department:
        print(employee)

