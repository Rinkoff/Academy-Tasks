number = "13436"
user_input = int(input("Enter a number:"))
i=0

while i < len(number):
    if user_input < int(number[i]):
        break
    print(number[i])
    i+=1