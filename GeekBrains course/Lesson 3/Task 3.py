'''
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''
import random as r

numbers = [r.randint(0,100) for i in range(10)]
max = numbers[0]
max_pos = 0
min = numbers[0]
min_pos = 0
print(f'Исходный массив: {numbers}')
for j, i in enumerate(numbers):
    if max<i:
        max = i
        max_pos = j
    if min>i:
        min = i
        min_pos = j
print(f'Максимальное число: {max}\nМинимальное число: {min}')
numbers[max_pos], numbers[min_pos] = min, max
print(f'Изменённый массив: {numbers}')