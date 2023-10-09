text = "Python is amazing"
count = 0
vowels = "aoueiAOUEI"

for char in text:
    if char in vowels:
        count+=1

print(count)

