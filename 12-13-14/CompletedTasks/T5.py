def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

result = is_palindrome("bob")
print(result)