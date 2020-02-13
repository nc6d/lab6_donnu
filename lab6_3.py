'''
3. За s-назвою місяця визначити відповідну пору року.
Виконав студент 1 курсу групи 122А Опанасюк Богдан
'''
from enum import Enum


class Month(Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12


class Season(Enum):
    Winter = 1
    Spring = 2
    Summer = 3
    Autumn = 4


flag = True
while flag == True:
    while True:
        try:
            s = Month[input('Input month name: ')].value
            break
        except KeyError:
            print('Enter correct month')
    if s == 12 or s < 3:
        print(Season.Winter.name)
    elif s < 6:
        print(Season.Spring.name)
    elif s < 9:
        print(Season.Summer.name)
    elif s < 12:
        print(Season.Autumn.name)
    else:
        print('Невірно введений місяць')

    print('Do you want to continue? (press "y" to continue)')
    text = input('')
    if text == 'y':
        flag = True
    else:
        flag = False
