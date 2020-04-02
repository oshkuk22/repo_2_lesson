




flag = True

while flag:
    try:
        items_list = int(input('Input the number of list items:'))
        flag = False

    except ValueError:
        print('Entered items_list is not a number!!!')