def is_valid(num):
    if num < 0:
        raise ValueError("Числото не е валидно")
    else:
        print("Числото е валидно")


is_valid(-2)
