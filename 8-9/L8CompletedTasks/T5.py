fruits =  ["apple", "banana", "apple", "orange", "banana", "apple", "grape"]

count = {}

for fruit in fruits:
    if fruit in count:
        count[fruit] += 1
    else:
        count[fruit] = 1

print(count)

