text = input("Enter a text:")
word_list = text.split(" ")

longest_word = ""

for word in word_list:
    if len(word) > len(longest_word):
        longest_word = word



print(longest_word)