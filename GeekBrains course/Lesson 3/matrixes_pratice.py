import random

size = 5
matrix = [[random.randint(1,10) for i in range(size)] for i in range(size)]
print(matrix)

for line in matrix:
    for char in line:
        print(f'{char:>4}', end='')
    print()

def sum_matrix():
    sum_column = [0]*size

    for line in matrix:
        sum_row = 0
        for i, char in enumerate(line):
            sum_row+=char
            sum_column[i] += char
            print(f'{char:>5}', end='')
        print(f'   | {sum_row}')
    print('-' *(len(matrix)*5))
    for k in sum_column:
        print(f'{k:>5}', end='')

def change_dioganal():
    for i in range(size):
        for j in range(size):
            if i==j:
                spam = matrix[i][j]
                matrix[i][j] = matrix[i][size-1-j]
                matrix[i][size-1-j] = spam
    print('-'*size*5)
