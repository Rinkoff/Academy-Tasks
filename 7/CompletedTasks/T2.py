numbers = [1,2,3,4,5]

print(len(numbers))

numbers.reverse()
print(numbers)

for number in numbers:
    print(number)

result = 0
for number in numbers:
    result += number

print(result)