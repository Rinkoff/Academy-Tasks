vowels = ["a","o","u","e","i","A","O","U",'E',"I"]

user_input = input("Enter a sentence:")
result = ""

for char in user_input:
    if char in vowels or char == " ":
        result += char

print(result)
