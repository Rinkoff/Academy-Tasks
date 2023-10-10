user_input = input("Enter some numbers, separated by spaces: ")
numbers = user_input.split()
max_number = int(numbers[0])

for num in numbers:
    if not num.isdigit():
        print("Enter only numbers")
        break
    else:
        if int(num) > max_number:
            max_number = int(num)

print("The largest number is:", max_number)