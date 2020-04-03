# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
# элемента — номер товара и словарь с параметрами (характеристиками товара: название,
# цена, количество, единица измерения). Структуру нужно сформировать программно, т.е.
# запрашивать все данные у пользователя. Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый
# ключ — характеристика товара, например название, а значение — список значений-характеристик,
# например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

# -*- coding: utf-8 -*-

flag = True

while flag:
    try:
        count_product = int(input(u'Input number of product varieties:'))
        flag = False

    except ValueError:
        print('Invalid value entered!!!')


product_list = list()

for i in range(count_product):
    product_dict = dict()
    num_one_prod = list()
    name_product = (input(f'Input the {i+1}th name of product:'))
    product_dict['name product'] = name_product

    flag = True

    while flag:
        try:
            price = int(input(f'Input price of {name_product} product:'))
            product_dict['price'] = price
            flag = False

        except ValueError:
            print('Invalid value entered!!!')

    flag = True

    while flag:
        try:
            number_of_product = int(input(f'number of product {name_product}:'))
            product_dict['number of product'] = number_of_product
            flag = False

        except ValueError:
            print('Invalid value entered!!!')

    measure_unit = input(f'Input measure unit {name_product}:')
    product_dict['measure unit'] = measure_unit

    num_one_prod.append(i + 1)
    num_one_prod.append(product_dict)

    product_list.append(tuple(num_one_prod))

print(product_list)

dict_in = dict()
name_list = list()
price_list = list()
count_list = list()
unit_list = list()
stat_dict = dict()

for j_tuple in product_list:
    dict_in = j_tuple[1]
    name_list.append(dict_in['name product'])
    price_list.append(dict_in['price'])
    count_list.append(dict_in['number of product'])
    unit_list.append(dict_in['measure unit'])
    stat_dict['name product'] = name_list
    stat_dict['price'] = price_list
    stat_dict['number of product'] = count_list
    stat_dict['measure unit'] = unit_list

print (stat_dict)



