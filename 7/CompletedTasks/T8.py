user_input = input("Enter some numbers, separated by spaces: ")
numbers = user_input.split()
number_list = []

for num in numbers:
    number_list.append(int(num))


ascending = sorted(number_list)
descending = sorted(number_list, reverse=True)

if number_list == ascending:
    print("Ascending order")
elif number_list == descending:
    print("Descending order")
else:
    print("Not in order")