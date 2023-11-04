content = input("Enter a text:")

with open("output.txt","w") as file:
    file.write(content)