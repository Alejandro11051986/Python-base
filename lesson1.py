#1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
a = 2
b = int(input("Введите число от 0 до 10:"))
while b > 10 or b < 0:
    print ('Условие не выполнено. Попробуйте еще раз')
    b = int(input("Введите число от 0 до 10:"))
else:
    c = (a + b)
    print("Если к вашему числу прибавить 2, получится", c)

#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
t = int(input('Введите время в секундах:'))
h=((t//3600))%24
m=(t//60)%60
s=t%60
if m<10:
    m=str('0'+str(m))
else:
    m=str(m)
if s<10:
    s=str('0'+str(s))
else:
    s=str(s)
print(str(h)+':'+str(m)+':'+str(s))

#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
n = int (input('введите целое число "n="'))
while True:
    n1 = n * 10 + n
    n2 = n * 100 + n1
    sum = (n + n1 + n2)
    if n > 0:
        print (('если сложить'), n, n1, n2,('получится -'), sum)
        break
    print ('введите число больше "0"')
    n = int(input('введите целое число "n="'))
#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
a = input ('целое положительное число не менее двух знаков a = ')
sheet = list (a)
print ('не понимаю как сделать это задание')

#5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
cashflow = int(input('введите  значение выручки='))
capex = int(input('введите значение издержек='))
a = cashflow - capex
b =  a / cashflow
if a < 0:
    print ('компания работает в минус')
else:
    print (a, ' , компания работает в плюс')
    print ('рентабельность компании=', b)
staff = int(input('введите количество сотрудников='))
c = a / staff
print (c)
#6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
#Например: a = 2, b = 3.
#Результат:
#1-й день: 2
#2-й день: 2,2
#3-й день: 2,42
#4-й день: 2,66
#5-й день: 2,93
#6-й день: 3,22
print ('с этим заданием тоже сложности - не понимаю как вообще подступиться к нему')
#Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

