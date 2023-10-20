def sum(a,b):
    print(a+b)

def ask_for_numbers():
    a = int(input("Въведете число:"))
    b = int(input("Въведете число:"))
    return a,b

try:
    a,b = ask_for_numbers()
    sum(a, b)
except ValueError as e:
    print("Грешка: Трябва да въведете число")
    print("Пробвайте отново")
    a,b = ask_for_numbers()
    sum(a, b)

