def is_anagram(word1,word2):
    if len(word1) != len(word2):
        return False

    list1 = list(word1)
    list2 = list(word2)

    list1.sort()
    list2.sort()

    if list1 == list2:
        return True
    else:
        return False

result = is_anagram("listen","silent")
print(result)