a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
c = int(input("Enter a number:"))


if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > a and c > b:
    print(c)
else:
    if c == a:
        print("c = a")
    elif b == a:
        print("b = a")
    elif b == c:
        print("b = c")
    else:
        print("a = b = c")