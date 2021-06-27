#Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
#Проверьте его работу на данных, вводимых пользователем.
#При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с
#ошибкой.

b = int(input('Введите цифру:'))


class ZeroDel(Exception):

    def __init__(self, txt):
        self.txt = txt


def start_test_except(a, b):
    try:
        if b == 0:
            raise ZeroDel("Делить на ноль нельзя")
        else:
            return a // b
    except ZeroDel as err:
        print(err)


print(start_test_except(10, b))
