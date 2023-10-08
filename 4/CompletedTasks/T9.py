month = input("Enter a month:")
place = input("Studio or Apartment:")
nights = int(input("How much nights will you spend:"))


if month == "January" or month == "February" or month == "March" or month == "April":
    if place == "Studio":
        print(nights * 50)
    elif place == "Apartment":
        print(nights * 65)
    else:
        print("Not valid place")
elif month == "May" or month == "June" or month == "July" or month == "August":
    if place == "Studio":
        print(nights * 100)
    elif place == "Apartment":
        print(nights * 130)
    else:
        print("Not valid place")
elif month == "September" or month == "October" or month == "November" or month == "December":
    if place == "Studio":
        print(nights * 70)
    elif place == "Apartment":
        print(nights * 90)
    else:
        print("Not valid place")
else:
    print("Not valid month")

