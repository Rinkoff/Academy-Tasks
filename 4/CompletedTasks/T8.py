a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
c = int(input("Enter a number:"))


if a > b and a > c:
    if b > c:
        print(a,b,c)
    else:
        print(a,c,b)
elif b > a and b > c:
    if a > c:
        print(b,a,c)
    else:
        print(b,c,a)
elif c > a and c > b:
    if a > b :
        print(c,a,b)
    else:
        print(c,b,a)
else:
    print("Some numbers are equal")

