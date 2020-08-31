'''
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
'''


import random as r

numbers = [r.randint(-50,5) for i in range(10)]
print(f'Исходный массив: {numbers}')

min = numbers[0]
max = numbers[0]
sum = 0
pos_max = 0
pos_min = 0
for i, k in enumerate(numbers):
    if k<min:
        min = k
        pos_min = i
    if k>max:
        max = k
        pos_max = i
if pos_min<pos_max:
    for j in range(pos_min+1, pos_max):
        sum+=numbers[j]
else:
    for j in range(pos_max+1, pos_min):
        sum+=numbers[j]
print(pos_min, pos_max)
print(f'Минимальный элемент: {min}\nМаксимальный элемент: {max}\nСумма чисел между ними: {sum}')