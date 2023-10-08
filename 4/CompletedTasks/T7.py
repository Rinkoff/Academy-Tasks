ages = int(input("Enter a dog ages:"))
dog_in_human_ages = 0

if ages == 0:
    dog_in_human_ages = 0
elif ages == 1:
    dog_in_human_ages = 1
elif ages == 2:
    dog_in_human_ages = 1 + 5
else:
    dog_in_human_ages = 1 + 5 + ((ages - 2) * 7)

print(dog_in_human_ages)
