'''4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.'''
words_str=input('введите несколько любых слов через пробел: ')
words_list=words_str.split()
for ind, el in enumerate(words_list):
    ind = ind + 1
    print(ind, el[0:10])
