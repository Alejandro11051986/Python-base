# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
user_number = abs(int(input('целое положительное число не менее двух знаков "a" = ')))
max_number = 0

while user_number > 0:
    item = user_number % 10
    if item >= max_number:
        max_number = item

    user_number = user_number // 10

print(max_number)
