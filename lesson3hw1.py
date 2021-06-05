'''1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.'''


def get_div(num_1, num_2):
    try:
        result = num_1 / num_2
    except ZeroDivisionError:
        return "Делить на ноль нельзя"
    return result


count_one = int(input('введите первое число:'))
count_two = int(input('введите второе число:'))
print('Результат деления первого числа на второе', get_div(count_one, count_two))
