raw_numbers = input("Enter some numbers:")

numbers_list_str = raw_numbers.split()
greater_num = 0
for num in numbers_list_str:
    if int(num) > greater_num:
        greater_num = int(num)

print(greater_num)