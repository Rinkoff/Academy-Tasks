user_input = input("Enter a text:")

count = {}

for char in user_input:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

most_frequently_encountered = max(count,key=count.get)

print(count)
print(most_frequently_encountered,":",count[most_frequently_encountered])
