message = "Hello"

def change_message(new_message):
    global message
    message = new_message


print(message)
change_message("hi")
print(message)