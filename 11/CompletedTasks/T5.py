raw_numbers = input("Enter five numbers:")

numbers_list_str = raw_numbers.split()
numbers_list = []
for num in numbers_list_str:
    numbers_list.append(int(num))

print(sum(numbers_list))