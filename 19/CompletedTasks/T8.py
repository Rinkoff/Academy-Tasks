try:
    with open("example.txt", "r") as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print("Файлът не съществува.")