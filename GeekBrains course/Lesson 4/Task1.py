'''
1. Проанализировать скорость и сложность одного любого алгоритма из разработанных 
в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать,
для каких N вы проводили замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему.
'''
#Задача взятая на оценивание:
#Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random as r
import cProfile
import functools
'''
Первый вариант 
'''
def min_elem1(size):
    matrix = [[r.randint(-5,5) for i in range(size)] for j in range(size)]
    #for line in matrix:
        #for char in line:
            #print(f'{char:>5}', end='')
        #print()

    min = []

    for i in matrix:
        min_num = i[0]
        for j in i:
            if j<min_num:
                min_num = j
        min.append(min_num)
    #print(f'Список минимальных элементов: {min}')
    max_num = min[0]
    for k in min:
        if k>max_num:
            max_num = k
    return max_num
    #print(f'Максимальный минимальный элемент: {max_num}')

'''
Анализ библиотекой timeit
size = 20, запускалась 100 раз
100 loops, best of 5: 524 usec per loop
size = 50, запускалась 100 раз
100 loops, best of 5: 3.25 msec per loop
size = 100, запускалась 100 раз
100 loops, best of 5: 13.5 msec per loop


Анализ библиотекой cProfile
При size = 20
2209 function calls in 0.001 seconds
1    0.000    0.000    0.001    0.001 Task1.py:10(min_elem1)

При size = 50
13737 function calls in 0.009 seconds
1    0.000    0.000    0.011    0.011 Task1.py:10(min_elem1)

При size = 100
54696 function calls in 0.031 seconds
1    0.001    0.001    0.039    0.039 Task1.py:10(min_elem1)
'''
########################################################################################
'''
Второй вариант 
'''
@functools.lru_cache
def min_elem2(size):
    matrix = [[r.randint(-5,5) for i in range(size)] for j in range(size)]
    #for line in matrix:
        #for char in line:
            #print(f'{char:>5}', end='')
        #print()

    min = []

    for i in matrix:
        min_num = i[0]
        for j in i:
            if j<min_num:
                min_num = j
        min.append(min_num)
    #print(f'Список минимальных элементов: {min}')
    max_num = min[0]
    for k in min:
        if k>max_num:
            max_num = k
    return max_num
    #print(f'Максимальный минимальный элемент: {max_num}')

'''
Анализ библиотекой timeit
size = 20, запускалась 100 раз
100 loops, best of 5: 141 nsec per loop
size = 50, запускалась 100 раз
100 loops, best of 5: 147 nsec per loop
size = 100, запускалась 100 раз
100 loops, best of 5: 160 nsec per loop


Анализ библиотекой cProfile
При size = 20
2242 function calls in 0.001 seconds
1    0.000    0.000    0.001    0.001 Task1.py:58(min_elem2)

При size = 50
13751 function calls in 0.007 seconds
1    0.000    0.000    0.007    0.007 Task1.py:58(min_elem2)

При size = 100
54751 function calls in 0.029 seconds
1    0.001    0.001    0.029    0.029 Task1.py:58(min_elem2)
'''
#######################################################################################
'''
Третий вариант 
'''
def min_elem3(size):
    matrix = [[r.randint(-5,5) for i in range(size)] for j in range(size)]
    #for line in matrix:
        #for char in line:
            #print(f'{char:>5}', end='')
        #print()

    min_num = []

    for i in matrix:
        min_num.append(min(i))
    #print(f'Список минимальных элементов: {min}')
    max_num = max(min_num)

'''
Анализ библиотекой timeit
size = 20, запускалась 100 раз
100 loops, best of 5: 525 usec per loop
size = 50, запускалась 100 раз
100 loops, best of 5: 3.35 msec per loop
size = 100, запускалась 100 раз
100 loops, best of 5: 12.9 msec per loop


Анализ библиотекой cProfile
При size = 20
2236 function calls in 0.001 seconds
1    0.000    0.000    0.001    0.001 Task1.py:113(min_elem3)

При size = 50
13637 function calls in 0.006 seconds
1    0.000    0.000    0.007    0.007 Task1.py:113(min_elem3)

При size = 100
54724 function calls in 0.026 seconds
1    0.000    0.000    0.031    0.031 Task1.py:113(min_elem3)
'''

#Вывод
"""
Лучше всех показал себя вариант номер 2, т.е. там, где использовался декоратор iru_cache
из библиотеки functools. На всех этапах он работал в быстрее и эффективнее. Два других варината
отработали почти индентично, т.к. количество проходов по спискам одинаково.
"""