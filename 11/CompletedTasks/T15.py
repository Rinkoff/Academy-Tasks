number = input("Enter a number with two or more digits:")

if number == number[::-1]:
    print("Is palindrome")
else:
    print("Not a palindrome")