#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def personal_data(name, surname, birthday, city, email, phone):
    return f'{name, surname, birthday, city, email, phone}'


user_name = input("Введите имя пользователя: ")
user_surname = input("Введите фамилию пользователя: ")
user_birthday = input("Введите дату рождения пользователя: ")
user_city = input("Введите город пользователя: ")
user_email = input("Введите e-mail пользователя: ")
user_phone = input("Введите телефон пользователя")

print(personal_data(name=user_name, surname=user_surname, birthday=user_birthday, city=user_city,
                    email=user_email, phone=user_phone))
