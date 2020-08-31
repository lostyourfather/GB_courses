'''
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
'''


import random as r

numbers = [r.randint(-50,5) for i in range(10)]
print(f'Исходный массив: {numbers}')

max_neg_num = 0
pos_num = 0
for k in numbers:
    if k<max_neg_num:
        max_neg_num = k
for i, j in enumerate(numbers):
    if j<0 and j>max_neg_num:
        max_neg_num = j
        pos_num = i
print(f'Максимальный отрицательный элемент: {max_neg_num}\nЕго позиция в массиве: {pos_num}')
