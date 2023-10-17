def max(numbers):
    greater = 0
    for num in numbers:
        if num > greater:
            greater = num

    return greater


numbers = [1,3,5,7,8,3,5]
result =  max(numbers)
print(result)