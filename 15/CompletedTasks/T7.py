names = ["Ivan", "Kate", "John"]

try:
    name = input("Въведете вашето име:")
    name = name.capitalize()
    if name not in names:
        raise ValueError("Нямате достъп до системата")
except ValueError as e:
    print(e)
else:
    print(f"Добре дошъл {name}")
finally:
    print("Искате ли да продължите")
