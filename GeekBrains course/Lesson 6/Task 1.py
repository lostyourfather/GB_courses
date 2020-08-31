'''
Выбранная задача на анализ:
8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать 
ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
'''
#Система и версия Python
#3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] win32
#С




import sys


print(sys.version, sys.platform)


#Функция для анализа
def mem(obj):
    print(f'Type: {obj.__class__}, size: {sys.getsizeof(obj)}, object{obj}')
    if hasattr(obj, '__iter__'):
        for i in obj:
            print('\t' + f'Type: {i.__class__}, size: {sys.getsizeof(i)}, object{i}')
            if hasattr(i, '__iter__'):
                for j in i:
                    print('\t' *2 + f'Type: {j.__class__}, size: {sys.getsizeof(j)}, object{j}')


#Реализация задачи 2
#Использование общего списка
matrix = []
for i in range(5):
    matrix.append([])
    for j in range(3):
        matrix[i].append(int(input('Введите число: ')))
    sum = 0
    for k in matrix[i]:
        sum+=k
    matrix[i].append(sum)
for line in matrix:
    for char in line:
        print(f'{char:>5}', end='')
    print()


'''
Type: <class 'list'>, size: 60, object[[5, 5, 5, 15], [5, 5, 5, 15], [5, 4, 6, 15], [7, 8, 9, 24], [4, 5, 8, 17]]
        Type: <class 'list'>, size: 44, object[5, 5, 5, 15]
                Type: <class 'int'>, size: 14, object5
                Type: <class 'int'>, size: 14, object5
                Type: <class 'int'>, size: 14, object5
                Type: <class 'int'>, size: 14, object15
        Type: <class 'list'>, size: 44, object[5, 5, 5, 15]
                Type: <class 'int'>, size: 14, object5
                Type: <class 'int'>, size: 14, object5
                Type: <class 'int'>, size: 14, object5
                Type: <class 'int'>, size: 14, object15
        Type: <class 'list'>, size: 44, object[5, 4, 6, 15]
                Type: <class 'int'>, size: 14, object5
                Type: <class 'int'>, size: 14, object4
                Type: <class 'int'>, size: 14, object6
                Type: <class 'int'>, size: 14, object15
        Type: <class 'list'>, size: 44, object[7, 8, 9, 24]
                Type: <class 'int'>, size: 14, object7
                Type: <class 'int'>, size: 14, object8
                Type: <class 'int'>, size: 14, object9
                Type: <class 'int'>, size: 14, object24
        Type: <class 'list'>, size: 44, object[4, 5, 8, 17]
                Type: <class 'int'>, size: 14, object4
                Type: <class 'int'>, size: 14, object5
                Type: <class 'int'>, size: 14, object8
                Type: <class 'int'>, size: 14, object17
'''



#Реализация задачи 2
#Без использование общего списка, но каждый ряд всё ещё отдельный список
mtx1 = []
mtx2 = []
mtx3 = []
mtx4 = []
mtx5 = []

for i in range(3):
        mtx1.append(int(input('Введите число 1-ой строки: ')))
        mtx2.append(int(input('Введите число 2-ой строки: ')))
        mtx3.append(int(input('Введите число 3-ей строки: ')))
        mtx4.append(int(input('Введите число 4-ой строки: ')))
        mtx5.append(int(input('Введите число 5-ой строки: ')))
mtx1.append(sum(mtx1))
mtx2.append(sum(mtx2))
mtx3.append(sum(mtx3))
mtx4.append(sum(mtx4))
mtx5.append(sum(mtx5))
print(mtx1,mtx2,mtx3,mtx4,mtx5, sep="\n")


'''
Type: <class 'list'>, size: 44, object[1, 1, 1, 3]
        Type: <class 'int'>, size: 14, object1
        Type: <class 'int'>, size: 14, object1
        Type: <class 'int'>, size: 14, object1
        Type: <class 'int'>, size: 14, object3
Type: <class 'list'>, size: 44, object[2, 2, 2, 6]
        Type: <class 'int'>, size: 14, object2
        Type: <class 'int'>, size: 14, object2
        Type: <class 'int'>, size: 14, object2
        Type: <class 'int'>, size: 14, object6
Type: <class 'list'>, size: 44, object[3, 3, 3, 9]
        Type: <class 'int'>, size: 14, object3
        Type: <class 'int'>, size: 14, object3
        Type: <class 'int'>, size: 14, object3
        Type: <class 'int'>, size: 14, object9
Type: <class 'list'>, size: 44, object[4, 4, 4, 12]
        Type: <class 'int'>, size: 14, object4
        Type: <class 'int'>, size: 14, object4
        Type: <class 'int'>, size: 14, object4
        Type: <class 'int'>, size: 14, object12
Type: <class 'list'>, size: 44, object[5, 5, 5, 15]
        Type: <class 'int'>, size: 14, object5
        Type: <class 'int'>, size: 14, object5
        Type: <class 'int'>, size: 14, object5
        Type: <class 'int'>, size: 14, object15
'''




#Реализация задачи 3
#Без использование общего списка, но каждый ряд это строка
mtx1 = ''
mtx2 = ''
mtx3 = ''
mtx4 = ''
mtx5 = ''
for i in range(3):
        mtx1=mtx1 + ' ' + input('Введите число 1-ой строки: ')
        mtx2=mtx2 + ' ' + input('Введите число 2-ой строки: ')
        mtx3=mtx3 + ' ' + input('Введите число 3-ей строки: ')
        mtx4=mtx4 + ' ' + input('Введите число 4-ой строки: ')
        mtx5=mtx5 + ' ' + input('Введите число 5-ой строки: ')
sum1 = sum(map(int, mtx1.split()))
sum2 = sum(map(int, mtx2.split()))
sum3 = sum(map(int, mtx3.split()))
sum4 = sum(map(int, mtx4.split()))
sum5 = sum(map(int, mtx5.split()))
mtx1 = mtx1 + ' ' + str(sum1)
mtx2 = mtx2 + ' ' + str(sum2)
mtx3 = mtx3 + ' ' + str(sum3)
mtx4 = mtx4 + ' ' + str(sum4)
mtx5 = mtx5 + ' ' + str(sum5)
print(mtx1,mtx2,mtx3,mtx4,mtx5, sep='\n')


'''
Type: <class 'str'>, size: 33, object 1 1 1 3
        Type: <class 'str'>, size: 26, object
                Type: <class 'str'>, size: 26, object
        Type: <class 'str'>, size: 26, object1
                Type: <class 'str'>, size: 26, object1
        Type: <class 'str'>, size: 26, object
                Type: <class 'str'>, size: 26, object
        Type: <class 'str'>, size: 26, object1
                Type: <class 'str'>, size: 26, object1
        Type: <class 'str'>, size: 26, object
                Type: <class 'str'>, size: 26, object
        Type: <class 'str'>, size: 26, object1
                Type: <class 'str'>, size: 26, object1
        Type: <class 'str'>, size: 26, object
                Type: <class 'str'>, size: 26, object
        Type: <class 'str'>, size: 26, object3
                Type: <class 'str'>, size: 26, object3
Type: <class 'str'>, size: 33, object 2 2 2 6
        Type: <class 'str'>, size: 26, object 
                Type: <class 'str'>, size: 26, object
        Type: <class 'str'>, size: 26, object2
                Type: <class 'str'>, size: 26, object2
        Type: <class 'str'>, size: 26, object
                Type: <class 'str'>, size: 26, object
        Type: <class 'str'>, size: 26, object2
                Type: <class 'str'>, size: 26, object2
        Type: <class 'str'>, size: 26, object
                Type: <class 'str'>, size: 26, object
        Type: <class 'str'>, size: 26, object2
                Type: <class 'str'>, size: 26, object2
        Type: <class 'str'>, size: 26, object
                Type: <class 'str'>, size: 26, object
        Type: <class 'str'>, size: 26, object6
                Type: <class 'str'>, size: 26, object6
Type: <class 'str'>, size: 33, object 3 3 3 9
        Type: <class 'str'>, size: 26, object
                Type: <class 'str'>, size: 26, object
        Type: <class 'str'>, size: 26, object3
                Type: <class 'str'>, size: 26, object3
        Type: <class 'str'>, size: 26, object
                Type: <class 'str'>, size: 26, object
        Type: <class 'str'>, size: 26, object3
                Type: <class 'str'>, size: 26, object3
        Type: <class 'str'>, size: 26, object
                Type: <class 'str'>, size: 26, object
        Type: <class 'str'>, size: 26, object3
                Type: <class 'str'>, size: 26, object3
        Type: <class 'str'>, size: 26, object
                Type: <class 'str'>, size: 26, object
        Type: <class 'str'>, size: 26, object9
                Type: <class 'str'>, size: 26, object9
Type: <class 'str'>, size: 34, object 4 4 4 12
        Type: <class 'str'>, size: 26, object
                Type: <class 'str'>, size: 26, object
        Type: <class 'str'>, size: 26, object4
                Type: <class 'str'>, size: 26, object4
        Type: <class 'str'>, size: 26, object 
                Type: <class 'str'>, size: 26, object
        Type: <class 'str'>, size: 26, object4
                Type: <class 'str'>, size: 26, object4
        Type: <class 'str'>, size: 26, object
                Type: <class 'str'>, size: 26, object
        Type: <class 'str'>, size: 26, object4
                Type: <class 'str'>, size: 26, object4
        Type: <class 'str'>, size: 26, object
                Type: <class 'str'>, size: 26, object
        Type: <class 'str'>, size: 26, object1
                Type: <class 'str'>, size: 26, object1
        Type: <class 'str'>, size: 26, object2
                Type: <class 'str'>, size: 26, object2
Type: <class 'str'>, size: 34, object 5 5 5 15
        Type: <class 'str'>, size: 26, object
                Type: <class 'str'>, size: 26, object
        Type: <class 'str'>, size: 26, object5
                Type: <class 'str'>, size: 26, object5
        Type: <class 'str'>, size: 26, object
                Type: <class 'str'>, size: 26, object
        Type: <class 'str'>, size: 26, object5
                Type: <class 'str'>, size: 26, object5
        Type: <class 'str'>, size: 26, object
                Type: <class 'str'>, size: 26, object
        Type: <class 'str'>, size: 26, object5
                Type: <class 'str'>, size: 26, object5
        Type: <class 'str'>, size: 26, object
                Type: <class 'str'>, size: 26, object
        Type: <class 'str'>, size: 26, object1
                Type: <class 'str'>, size: 26, object1
        Type: <class 'str'>, size: 26, object5
                Type: <class 'str'>, size: 26, object5
'''

#Вывод
'''
С точки зрения используемой памяти предпочтителен вариант 2, так как там нет общего списка и все данные
в субсписках хранятся в int. С точки зрения универсальности программы, реализация плоха, так как мы вручную
создаём переменные для каждого ряда.
Хуже всех себя показал вариант 3, так как str сам по себе занимает больше памяти, так ещё и пробелы в строке
считаются отдельными символами и занимают память, а про сложность и неудобность подобного решения и говорить
не стоит.
'''