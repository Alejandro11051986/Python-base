'''2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().'''
some_list = input('введите полное Имя, Фамилию, год рождения, страну проживания: ')
some_list = some_list.split()
step = 0
for i in range(int(len(some_list)/2)):
    some_list[step], some_list[step+1] = some_list[step+1], some_list[step]
    step += 2
print(some_list)