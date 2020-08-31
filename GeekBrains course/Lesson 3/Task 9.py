'''
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
'''



import random as r

matrix = [[r.randint(-5,5) for i in range(5)] for j in range(5)]
for line in matrix:
    for char in line:
        print(f'{char:>5}', end='')
    print()

min = []

for i in matrix:
    min_num = i[0]
    for j in i:
        if j<min_num:
            min_num = j
    min.append(min_num)
print(f'Список минимальных элементов: {min}')
max_num = min[0]
for k in min:
    if k>max_num:
        max_num = k
print(f'Максимальный минимальный элемент: {max_num}')