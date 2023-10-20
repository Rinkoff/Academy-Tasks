def divide(x, y):
    if y == 0:
        raise ValueError("Деление на нула не е позволено")
    return x / y

x = int(input("Въведете число:"))
y = int(input("Въведете число:"))
result = divide(x, y)

