'''
Задание
7. Определить, является ли год, который ввел пользователь,
високосным или не високосным.
'''
year = int(input('Введите номер года: '))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f'{year} год високосный')
        else:
            print(f'{year} год не високосный')
    else:
        print(f'{year} год високосный')
else:
    print(f'{year} год не високосный')