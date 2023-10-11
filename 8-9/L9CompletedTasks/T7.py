week_days = [
    ("Понеделник", "Работен"),
    ("Вторник", "Работен"),
    ("Сряда", "Работен"),
    ("Четвъртък", "Работен"),
    ("Петък", "Работен"),
    ("Събота", "Почивен"),
    ("Неделя", "Почивен"),
]

work_days = 0
rest_days = 0
for day in week_days:
    if day[1] == "Работен":
        work_days += 1
    elif day[1] == "Почивен":
        rest_days += 1

print("Work days are",work_days)
print("Rest days are",rest_days)