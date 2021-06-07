# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, work_time, rate_hours, bonus = argv


def get_salary (production_ph, rate_ph, prize_e):
    salary = int(production_ph) * int(rate_ph) + int(prize_e)
    return salary


print(get_salary(work_time, rate_hours, bonus))
