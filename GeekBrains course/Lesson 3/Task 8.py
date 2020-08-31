'''
8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать 
ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
'''


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

