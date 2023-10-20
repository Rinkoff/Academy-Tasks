whole_list = [1,2,3,4,5,6,7,8,9]

def divide_list(list):
    even = []
    odd = []

    for el in list:
        if el % 2 == 0:
            even.append(el)
        elif el % 2 != 0:
            odd.append(el)
        else:
            raise ValueError("Списъка трябва да съдържа само числа")

    if len(even) == 0:
        raise ValueError("Няма четни числа")
    if len(odd) == 0:
        raise ValueError("Няма нечетни числа")

    print(f"Четните числа са:{even}")
    print(f"Нечетните числа са:{odd}")


divide_list(whole_list)
