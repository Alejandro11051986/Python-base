# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


def int_func(word):
    """
    Функция проверяет что слово введено согласно условиям и делает первую букву слова заглавной.
    word -- string, default value -- None
    """
    result = ""
    for letter in word:
        if 97 <= ord(letter) <= 122:
            result += letter
        else:
            result = ""
            break
    return result.title()


def make_words_title():
    """Функция раскладывает строку на элементы и возвращает строку, где каждое слово с заглавной буквы."""
    user_input = input("Введите строку из латинских слов, разделенные пробелом. Все слова должны быть lowercase: ")
    data_list = user_input.split(" ")
    result_string = ""
    for words in data_list:
        result_string += int_func(words) + " "
    return result_string[0:-1]


print(make_words_title())
