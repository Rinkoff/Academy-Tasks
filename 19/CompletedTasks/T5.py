adittional_text = input("Enter a text:")

with open("example.txt","a") as file:
    file.write(adittional_text)