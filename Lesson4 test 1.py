# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


def my_func (production_ph, rate_ph, prize_e):
    result = (production_ph*rate_ph) + prize_e
    return result


print(my_func(8, 100, 500))