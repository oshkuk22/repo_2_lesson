# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

# list

m_list = ['January-Winter', 'February-Winter', 'March-Spring', 'April-Spring', 'May-Spring',
          'June-Summer', 'July-Summer', 'August-Summer', 'September-Autumn', 'October-Autumn',
          'November-Autumn', 'December-Winter']

flag = True

while flag:
    try:
        number_m = int(input('Input the number of list items:'))

        if (number_m > 0) and (number_m<13):
            if number_m < 3 or number_m ==12:
                print(f'mounth: {m_list[number_m-1].split("-")[0]}, season: {m_list[number_m-1].split("-")[1]}')
                flag = False
            elif (number_m >= 3) and (number_m<6):
                print(f'mounth: {m_list[number_m-1].split("-")[0]}, season: {m_list[number_m-1].split("-")[1]}')
                flag = False
            elif (number_m >= 6) and (number_m<9):
                print(f'mounth: {m_list[number_m-1].split("-")[0]}, season: {m_list[number_m-1].split("-")[1]}')
                flag = False
            else:
                print(f'mounth: {m_list[number_m-1].split("-")[0]}, season: {m_list[number_m-1].split("-")[1]}')
                flag = False
        else:
            print(f'No month with the number {number_m}' )

    except ValueError:
        print('Entered number mouth is not a number!!!')

# dict
m_dict = {'January': 'Winter', 'February': 'Winter', 'March': 'Spring', 'April': 'Spring', 'May': 'Spring',
          'June': 'Summer', 'July': 'Summer', 'August': 'Summer', 'September': 'Autumn', 'October': 'Autumn',
          'November': 'Autumn', 'December': 'Winter'}


flag = True

while flag:
    try:
        number_m = int(input('Input the number of list items:'))

        if (number_m > 0) and (number_m<13):
            if number_m < 3 or number_m ==12:
                print(f'mounth: {list(m_dict.keys())[number_m-1]}, '
                      f'season: {m_dict.get(list(m_dict.keys())[number_m-1])}')
                flag = False
            elif (number_m >= 3) and (number_m<6):
                print(f'mounth: {list(m_dict.keys())[number_m-1]}, '
                      f'season: {m_dict.get(list(m_dict.keys())[number_m-1])}')
                flag = False
            elif (number_m >= 6) and (number_m<9):
                print(f'mounth: {list(m_dict.keys())[number_m-1]},'
                      f' season: {m_dict.get(list(m_dict.keys())[number_m-1])}')
                flag = False
            else:
                print(f'mounth: {list(m_dict.keys())[number_m-1]}, '
                      f'season: {m_dict.get(list(m_dict.keys())[number_m-1])}')
                flag = False
        else:
            print(f'No month with the number {number_m}')

    except ValueError:
        print('Entered number mouth is not a number!!!')