'''
9. Среди натуральных чисел, которые были введены, 
найти наибольшее по сумме цифр. Вывести на экран это
число и сумму его цифр.
'''
max = 0
sum = 0
while True:
    num = input('Введите число: ')
    num_s = 0
    for i in num:
        num_s+=int(i)
    if num_s>sum:
        sum = num_s
        max = num
    ans = input('Будет ещё число? ')
    if ans == 'да':
        continue
    print(f'Наибольшее число {max}\n Сумма его чисел {sum}')
    break