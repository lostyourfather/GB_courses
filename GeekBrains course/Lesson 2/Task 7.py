"""
7. Написать программу, доказывающую или проверяющую,
 что для множества натуральных чисел выполняется равенство:
  1+2+...+n = n(n+1)/2, где n — любое натуральное число.
"""
n = int(input('Введите число: '))
left_side = 0
for i in range(n+1):
    left_side+=i
right_side = n*(n+1)/2
if left_side==right_side:
    print('Всё верно')
else:
    print('Неверно')