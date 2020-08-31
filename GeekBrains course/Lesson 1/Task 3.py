import random

int_num1 = int(input('Введите первое целое число: '))
int_num2 = int(input('Введите второе целое число: '))
float_num1 = float(input('Введите первое вещественное число: '))
float_num2 = float(input('Введите первое вещественное число: '))
letter1 = input('Введите первую букву: ')
letter2 = input('Введите вторую букву: ')

print(f'Случайное целое число в диапазоне от {int_num1} до {int_num2}: {random.randint(int_num1,int_num2)}')
print(f'Случайное вещественное число в диапазоне от {float_num1} до {float_num2}: {random.uniform(float_num1,float_num2)}')
print(f'Случайная буква от {letter1} до {letter2}: {chr(random.randint(ord(letter1), ord(letter2)))}')