# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
# с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [20, 19, 19, 9, 8, 7, 6, 6, 6, 6, 6, 6,5, 5, 4, 4, 3, 2, 1]
flag = True
print(my_list)
while flag:
    try:
        rat_val = int(input('Input the rating value:'))
        flag = False

    except ValueError:
        print('Entered items_list is not a number or not a integer!!!')
i = 0
flag_min = False


while i < len(my_list):
    if rat_val > my_list[i]:
        my_list.insert(i, rat_val)
        flag_min = True
        break
    else:
        i += 1

if not flag_min:
    my_list.insert(i, rat_val)

print(my_list)



