# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

my_list = [item for item in range(100, 1001) if (item % 2) == 0]


def multiplying_num(x, y):
    return x * y


result = reduce(multiplying_num, my_list)
