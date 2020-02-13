'''
2. Значення змінної x, що позначає деяку суму грошей в валюті p, замінити величиною
цієї ж суми в гривнях.
Виконав студент 1 курсу групи 122А Опанасюк Богдан
'''
from enum import Enum


class Converter(Enum):
    USD = 1
    EUR = 2
    CZK = 3
    PLN = 4


flag = True
while flag == True:
    while True:
        try:
            x = float(input('AMOUNT OF MONEY: '))
            p = Converter[input('currency:')]
            break
        except KeyError:
            print('Enter correct amount')
        except ValueError:
            print('Enter correct amount')
    if p == Converter.USD:
        print(x / 24.2582)
    elif p == Converter.EUR:
        print(x / 26.4041)
    elif p == Converter.CZK:
        print(x / 1.07573784)
    elif p == Converter.PLN:
        print(x / 6.3050)
    else:
        print('Input correct data!')

    print('Do you want to continue? (press "y" to continue)')
    text = input('')
    if text == 'y':
        flag = True
    else:
        flag = False
