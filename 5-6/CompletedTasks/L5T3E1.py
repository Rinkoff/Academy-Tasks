text = "Python is amazing"
count = 0
vowels = "aoueiAOUEI"

i = 0

while i < len(text):
    if text[i] in vowels:
        count+=1
    i+=1

print(count)