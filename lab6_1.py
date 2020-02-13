'''
1. За датою d, m, y визначити дату наступного і попереднього дня. В програмі врахувати
наявність високосних років.
Виконав студент 1 курсу групи 122А Опанасюк Богдан
'''
days = range(1, 32)
months = range(1, 13)
years = range(1901, 2020)
flag = True
while flag:
    while True:
        try:
            d, m, y = int(input('Day: ')), \
                      int(input('Month: ')), \
                      int(input('Year: '))
            break
        except ValueError:
            print('Enter correct number')

    if d in days and m in months and y in years:
        if y % 4 == 0:
            if d == 31 and (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
                if m == 12:
                    m = 0
                    y_2 = y + 1
                    m_2 = m + 1
                    print(f'Наступний: 1.{m_2}.{y_2}')
                    print(f'Попередній: {d - 1}.12.{y}')

                else:
                    if m == 1:
                        print(f'Наступний: 1.{m + 1}.{y}')
                        print(f'Попередній: {d - 1}.{m}.{y}')
                    else:
                        print(f'Наступний: 1.{m + 1}.{y}')
                        print(f'Попередній: {d - 1}.{m - 1}.{y}')
            elif d == 29 and m == 2:
                print(f'Наступний: 28.2.{y}')
                print(f'Попередній: 1.3.{y}')
            elif d == 30 and (m == 4 or m == 6 or m == 9 or m == 11):
                print(f'Наступний: 29.{m}.{y}')
                print(f'Попередній: 1.{m}.{y}')
            else:
                if d == 1:
                    if (m == 4 or m == 6 or m == 8 or m == 9 or m == 11 or m == 1 or m == 2):
                        print(f'Попередній: 31.{m - 1}.{y}')
                        print(f'Наступний: {d + 1}.{m}.{y}')
                    elif (m == 5 or m == 10 or m == 12 or m == 7):
                        print(f'Попередній: 30.{m - 1}.{y}')
                        print(f'Наступний: {d + 1}.{m}.{y}')
                    else:
                        print(f'Попередній: 29.{m - 1}.{y}')
                        print(f'Наступний: {d + 1}.{m}.{y}')
                else:
                    print(f'Попередній: {d - 1}.{m}.{y}')
                    print(f'Наступний: {d + 1}.{m}.{y}')


        else:
            if d == 31 and (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
                if m == 12:
                    m = 0
                    y_2 = y + 1
                    m_2 = m + 1
                    print(f'Наступний: 1.{m_2}.{y_2}')
                    print(f'Попередній: {d - 1}.12.{y}')
                else:
                    if m == 1:
                        print(f'Наступний: 1.{m + 1}.{y}')
                        print(f'Попередній: {d - 1}.{m}.{y}')
                    else:
                        print(f'Наступний: 1.{m + 1}.{y}')
                        print(f'Попередній: {d - 1}.{m}.{y}')
            elif d == 28 and m == 2:
                print(f'Наступний: 27.2.{y}')
                print(f'Попередній: 1.3.{y}')
            elif d == 30 and (m == 9 or m == 4 or m == 6 or m == 11):
                print(f'Наступний: 29.{m}.{y}')
                print(f'Попередній: 1.{m}.{y}')
            else:
                if d == 1:
                    if (m == 4 or m == 6 or m == 8 or m == 9 or m == 11 or m == 1 or m == 2):
                        print(f'Попередній: 31.{m - 1}.{y}')
                        print(f'Наступний: {d + 1}.{m}.{y}')
                    elif (m == 5 or m == 10 or m == 12 or m == 7):
                        print(f'Попередній: 30.{m - 1}.{y}')
                        print(f'Наступний: {d + 1}.{m}.{y}')
                    else:
                        print(f'Попередній: 28.{m - 1}.{y}')
                        print(f'Наступний: {d + 1}.{m}.{y}')
                else:
                    print(f'Попередній: {d - 1}.{m}.{y}')
                    print(f'Наступний: {d + 1}.{m}.{y}')

    print('Do you want to continue? (press "y" to continue)')
    text = input('')
    if text == 'y':
        flag = True
    else:
        flag = False
