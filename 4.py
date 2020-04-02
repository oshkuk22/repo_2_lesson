# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

entered_string = (input('Input the number of list items:'))
list_string = entered_string.split(" ")

for i in range(len(list_string)):

    if len(list_string[i]) > 10:
        print(f'{i+1}th word: {list_string[i][:10]}')

    else:
        print(f'{i + 1}th word: {list_string[i]}')




