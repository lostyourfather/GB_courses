'''
Задача
2. По введенным пользователем координатам двух точек вывести
уравнение прямой вида y = kx + b, проходящей через эти точки.
'''

x1 = float(input('Введите координату x первой точки: '))
y1 = float(input('Введите координату y первой точки: '))
x2 = float(input('Введите координату x второй точки: '))
y2 = float(input('Введите координату y второй точки: '))
k = (y1-y2)/(x1-x2)
b = y2-k*x2
print(f'Итоговое уравнение имеет следущий вид: y = {k}*x + {b}')