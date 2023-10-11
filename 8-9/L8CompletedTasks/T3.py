user_input = input("Enter a word:")

count = {}

for char in user_input:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

print(count)

