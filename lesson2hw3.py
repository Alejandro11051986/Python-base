'''3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.'''
list_winter = [12, 1, 2]
list_spring = [3, 4, 5]
list_summer = [6, 7, 8]
list_autumn = [9, 10, 11]
month = int(input('введите любой месяц цифровым значением от 0 до 12 :'))
if month in list_autumn:
    print('осень')
elif month in list_summer:
    print('лето')
elif month in list_spring:
    print('весна')
elif month in list_winter:
    print('зима')
else:
    print('нет такого месяца')

dict_seasons = {'winter': (12, 1, 2), 'spring' : (3, 4, 5), 'summer' : (6, 7, 8), 'autumn' : (9, 10, 11)}
month = int(input('введите любой месяц цифровым значением от 0 до 12 :'))
if month in dict_seasons.get('winter'):
    print('winter')
elif month in dict_seasons.get('spring'):
    print('spring')
elif month in dict_seasons.get('summer'):
    print('summer')
else:
    print('autumn')




