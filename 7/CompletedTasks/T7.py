fruits = ["apple", "pear", "banana", "orange", "apple", "apple", "orange", "pineapple"]

filtered_fruits = []

for fruit in fruits:
    if fruit not in filtered_fruits:
        filtered_fruits.append(fruit)

print(filtered_fruits)