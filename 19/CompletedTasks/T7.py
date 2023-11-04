with open("example.txt","r") as file:
    content = file.read()

numbers = []
for num in content.split():
    numbers.append(int(num))

average = sum(numbers) / len(numbers)

print(average)
