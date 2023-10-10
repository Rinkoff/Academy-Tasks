user_input = input("Enter some numbers, separated by spaces: ")
numbers = user_input.split()
even_numbers = []

for num in numbers:
    if not num.isdigit():
        print("Enter only numbers")
        break
    else:
        if int(num) % 2 == 0:
            even_numbers.append(num)

print(even_numbers)