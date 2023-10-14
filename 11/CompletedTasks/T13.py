raw_numbers = input("Enter five numbers:")

numbers_list_str = raw_numbers.split()
numbers_list = []
for num in numbers_list_str:
    numbers_list.append(int(num))

average_num = sum(numbers_list) / len(numbers_list)
print(f"Average number is {average_num}")

for num in numbers_list:
    if num > average_num:
        print(num)