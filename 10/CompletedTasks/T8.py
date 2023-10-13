number = input("Enter a five digits number:")

number_list = []

if len(number) == 5 and number.isdigit():
    for digit in number:
        number_list.append(int(digit))
    print(sum(number_list))
else:
    print("We need five digits number!")
