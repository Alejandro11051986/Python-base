#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(num_1, num_2, num_3):
    max_sum_num = [num_1, num_2, num_3]
    max_sum_num.remove(min(max_sum_num))
    return sum(max_sum_num)


print(my_func(9, 3, 7))
