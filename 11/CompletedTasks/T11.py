words = input("Enter some words:")

words_list = words.split()

for word in words_list:
    if len(word) > 5:
        print(word)