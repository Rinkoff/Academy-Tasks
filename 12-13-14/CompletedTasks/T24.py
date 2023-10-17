def check_and_get_position(numbers_list, number):
    if number in numbers_list:
        position = numbers_list.index(number)
        return position + 1
    else:
        print(f"Числото {number} не се съдържа в списъка.")
        return None

numbers = [1, 5, 10, 15, 20]
num = 10
result = check_and_get_position(numbers, num)
if result is not None:
    print(f"Числото {num} се намира на позиция {result}.")