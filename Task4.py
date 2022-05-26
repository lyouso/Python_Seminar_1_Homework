# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат 
# точек в этой четверти (x и y).

number = int(input('Введите номер четверти: '))
if number > 0 and number < 5:
    if number == 1:
        print('0 < x < +infinity')
        print('0 < y < +infinity')
    elif number == 2:
        print('-infinity < x < 0')
        print('0 < y < +infinity')
    elif number == 3:
        print('-infinity < x < 0')
        print('-infinity < y < 0')
    elif number == 4:
        print('0 < x < +infinity')
        print('-infinity < y < 0')