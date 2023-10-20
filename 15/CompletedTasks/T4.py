from math import *

def square_root(num):
    if num < 0:
        raise ValueError("Не може да се изчисли квадратен корен от отринцателно число!")

    return int(sqrt(num))


print(square_root(9))