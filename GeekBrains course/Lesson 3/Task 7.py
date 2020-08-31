'''
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
'''



import random as r

numbers = [r.randint(-5,5) for i in range(10)]
print(f'Исходный массив: {numbers}')

min1 = numbers[0]


for i in numbers:
    if i<min1:
        min1 = i
numbers.remove(numbers[numbers.index(min1)])
print(numbers)
min2 = numbers[0]
for j in numbers:
    if j<min2:
        min2 = j
print(f'Первое минимальное значение: {min1}\nВторое минимальное значение: {min2}')