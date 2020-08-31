'''
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и 
возвращать соответствующее простое число. Проанализировать скорость и сложность 
алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Второй — без использования «Решета Эратосфена».
'''
import cProfile
def sieve_erat(n):
    m = [i for i in range(n+1)]
    m[1] = 0
    for i in range(2,n):
        if m[i]!=0:
            j = i*2
            while j<=n:
                m[j] = 0
                j+=i
    simple_num = [i for i in m if i!=0]
    return simple_num[-1]
#Оценка поиска простых чисел через решето
"""
n = 20, запускался 100 раз
100 loops, best of 5: 7.36 usec per loop
n = 50, запускался 100 раз
100 loops, best of 5: 17.1 usec per loop
n = 100, запускался 100 раз
100 loops, best of 5: 33.4 usec per loop
n = 1000, запускался 100 раз
100 loops, best of 5: 455 usec per loop
n = 20, через cProfile
6 function calls in 0.000 seconds
1    0.000    0.000    0.000    0.000 Task2.py:2(sieve_erat)
6 function calls in 0.000 seconds
1    0.000    0.000    0.000    0.000 Task2.py:2(sieve_erat)
6 function calls in 0.000 seconds
1    0.000    0.000    0.000    0.000 Task2.py:2(sieve_erat)
"""
#Оценка сложности
'''
Сложность данного алгоритма можно охарактеризовать как O(n), так как время увеличивается
пропорционально увеличению входного значения
'''

def simple_num(i):
    numb_list = [2]
    number = 3
    while len(numb_list) < i:
        flag = True
        for j in numb_list:
            if number % j == 0:
                flag = False
                break
        if flag:
            numb_list.append(number)
        number += 1
    return numb_list[-1]
#Оценка поиска простых чисел через иной алгоритм
"""
n = 20, запускался 100 раз
100 loops, best of 5: 35.3 usec per loop
n = 50, запускался 100 раз
100 loops, best of 5: 156 usec per loop
n = 100, запускался 100 раз
100 loops, best of 5: 539 usec per loop
n = 1000, запускался 100 раз
100 loops, best of 5: 48.2 msec per loop
n = 20, через cProfile
93 function calls in 0.000 seconds
1    0.000    0.000    0.000    0.000 Task2.py:29(simple_num)
281 function calls in 0.000 seconds
1    0.000    0.000    0.000    0.000 Task2.py:29(simple_num)
643 function calls in 0.001 seconds
1    0.001    0.001    0.001    0.001 Task2.py:29(simple_num)
"""
#Оценка сложности
"""
Сложность данного алгоритма можно охарактеризовать как O(n^2), так как время увеличивается
пропорционально квадратичной функции. Следовательно, решето при сравнении является более
эффективным методом поиска простого числа
"""
print(sieve_erat(2))
print(simple_num(4))