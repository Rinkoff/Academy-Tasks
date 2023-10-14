words = input("Enter some words:")

words_list = words.split()
words_dict = {}
key = 0

for word in words_list:
    words_dict[key]=word
    key += 1


print(words_dict)

# for i,word in enumerate(words_list):
#     words_dict[i] = word
#
# print(words_dict)