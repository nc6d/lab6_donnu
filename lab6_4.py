'''
4. Робота світлофора для водіїв запрограмована таким чином: на початку кожної
години протягом трьох хвилин горить зелений сигнал, потім протягом однієї хвилини -
жовтий, протягом двох хвилин - червоний, протягом трьох хвилин - знову зелений і т. д.
Розробити програму, яка вводить дійсне число t, що означає час в хвилинах, що
минув з початку чергової години і визначає сигнал якого кольору горить для водіїв в цей
момент.
Виконав студент 1 курсу групи 122А Опанасюк Богдан
'''
flag1 = True
while flag1:
    while True:
        try:
            t = int(input('Time in minutes: '))
            break
        except ValueError:
            print('Please, write an integer')

    if 0 <= t % 6 < 3:
        print('Green')
    elif 3 <= t % 6 < 4:
        print('Yellow')
    elif 4 <= t % 6 < 5:
        print('Red')

    print('Program is executed')
    text = input('Do u wanna run it once more? (Input "y" or "n"): ')
    if text == 'y':
        flag1 = True
    if text == 'n':
        flag1 = False
