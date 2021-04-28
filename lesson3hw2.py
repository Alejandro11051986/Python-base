#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


def personal_data(name, surname, birthday, city, email, phone):
    return f'{name, surname, birthday, city, email, phone}'


print(personal_data(name='Алексей', surname='Штырняев', birthday='1990', city='Москва',
                    email='geekbrains@pochta.ru', phone='8(955) 555-55-55'))