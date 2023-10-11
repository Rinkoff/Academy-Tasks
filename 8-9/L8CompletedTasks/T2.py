basket = {
    "apples":1.20,
    "bananas":3.9,
    "oranges":4.6,
    "pears":2
}

total_price = 0

for price in basket.values():
    total_price += price

print(total_price)