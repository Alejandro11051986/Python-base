#6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию
# об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
#Пример готовой структуры:
#[
#(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
#]
#Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
#Пример:
#{
#“название”: [“компьютер”, “принтер”, “сканер”],
#“цена”: [20000, 6000, 2000],
#“количество”: [5, 2, 7],
#“ед”: [“шт.”]
#}
products_matrix = {"название": None,
                   "цена": None,
                   "количество": None,
                   "ед": None
                   }
number_iterations = 3
position_number = 0
data_input = [{}, {}, {}]
products_list = []
product_name = []
product_price = []
product_count = []
product_piece = []

while position_number is not number_iterations:
    data_input[position_number].update({"название": input("Введите название продукта: "),
                                        "цена": input("Введите цену продукта: "),
                                        "количество": input("Введите количество продукта: "),
                                        "ед": input("Введите ед. измерения продукта: ")
                                        })
    position_number += 1

for input_index, input_val in enumerate(data_input, 1):
    products_list.append((input_index, input_val))

for product_index, product_value in enumerate(products_list):
    product_name.append(product_value[1].get("название"))
    product_price.append(product_value[1].get("цена"))
    product_count.append(product_value[1].get("количество"))
    product_piece.append(product_value[1].get("ед"))

products_matrix.update({"название": product_name,
                        "цена": product_price,
                        "количество": product_count,
                        "ед": product_piece
                        })
print(products_matrix)

index = 1
result = []
spec = ["название", "цена", "количество", "цвет"]

while True:
    question = input("Добавить новый продукт да/нет?") # нет Нет нЕт НЕт НеТ НЕТ
    if question.upper() == "НЕТ":
        break
    item = {} #dict

    for spe in spec:
        user_data = input(f"Введите {spe}")
        #item[spe] == int(user_data) if user_data.isdigit() else user_data
        if user_data.isdigit(): #True or False
            item[spe] = int(user_data)
        else:
            item[spe] = user_data

    result.append(tuple([index,item]))
    index +=1
print(result)

res_dict = {}
for item in spec:
    for _, param in result:
        if res_dict.get(item):
            res_dict[].append(param.get(item))
        else