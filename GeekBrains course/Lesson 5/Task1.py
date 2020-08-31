'''
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, чья
прибыль выше среднего и ниже среднего.
'''
from collections import namedtuple
Company = namedtuple('Company', 'name, money')
list_company = []
n = int(input('Сколько предприятий будет: '))
for i in range(n):
    name = input('Введите название предприятия: ')
    money = 0
    for k in range(4):
        money += int(input(f'Введите прибыль в {k+1}-ом квартале: '))
    list_company.append(Company(name, money))
middle_money = 0
for j in range(n):
    middle_money+=list_company[j].money
middle_money/=n
print(f'Средний доход предприятий: {middle_money}')
for m in range(n):
    if middle_money>list_company[m].money:
        print(f'{list_company[m].name} меньше среднего заработка в год - {list_company[m].money}')
    elif middle_money<list_company[m].money:
        print(f'{list_company[m].name} больше среднего заработка в год - {list_company[m].money}')

