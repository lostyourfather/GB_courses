'''2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] 
соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''
from collections import deque

def num_to_lst(num):
    lst_num = []
    for i in num:
        lst_num.append(i)
    return lst_num

def lst_to_ten(lst_num):
    global dct_16
    num = 0
    for i, j in enumerate(lst_num):
        num += dct_16[j]*(16**(len(lst_num)-1-i))
    return num

def ten_to_lst(num):
    global rev_dtc_16
    lst = deque()
    while True:
        lst.appendleft(rev_dtc_16[str(num%16)])
        num = num//16
        if num//16 == 0:
            lst.appendleft(rev_dtc_16[str(num%16)])
            return lst
dct_16 = {'0': 0, '1':1, '2':2,'3':3, '4':4,'5':5, '6':6,'7':7, '8':8,'9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
rev_dtc_16 = {'0': 0, '1':1, '2':2,'3':3, '4':4,'5':5, '6':6,'7':7, '8':8,'9':9, '10':'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}

num_1 = input('Введите число в 16-ой с/с: ')
num_2 = input('Введите число в 16-ой с/с: ')

lst_num_1 = num_to_lst(num_1)
lst_num_2 = num_to_lst(num_2)

num_1 = lst_to_ten(lst_num_1)
num_2 = lst_to_ten(lst_num_2)
sum = num_1+num_2
mult = num_1*num_2

sum = list(ten_to_lst(sum))
mult = list(ten_to_lst(mult))

print(f'Сумма чисел: {sum}\nПроизведение чисел: {mult}')

