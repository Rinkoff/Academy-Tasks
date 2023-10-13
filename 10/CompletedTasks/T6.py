import random

pass_len = int(input("Enter the desired length for your password:"))

password = ""

for _ in range(pass_len):
    random_num = random.randint(1,9)
    password += str(random_num)


print(password)