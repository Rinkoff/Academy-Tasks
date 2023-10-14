text = input("Enter a text:")

letter_count = {}
for char in text:
    if char.isalpha():
        char_lower = char.lower()
        if char_lower in letter_count:
            letter_count[char_lower] += 1
        else:
            letter_count[char_lower] = 1

most_common = max(letter_count, key=letter_count.get)
print(f"{most_common} : {letter_count[most_common]}")