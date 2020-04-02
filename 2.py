# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list =list()

flag = True

while flag:
    try:
        items_list = int(input('Input the number of list items:'))
        flag = False

    except ValueError:
        print('Entered items_list is not a number!!!')

for i in range(items_list):
    try:
        items_list = (input(f'Input the {i+1}th number of list items:'))
        my_list.append(int(items_list))
    except ValueError:
        my_list.append(items_list)

print(my_list)

if len(my_list)%2 == 0:
     my_list[::2], my_list[1::2] = my_list[1::2], my_list[::2]

else:
    my_list[:-1:2], my_list[1:-1:2] = my_list[1:-1:2], my_list[:-1:2]

print(my_list)