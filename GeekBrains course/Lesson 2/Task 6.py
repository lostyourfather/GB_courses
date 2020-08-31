"""
6. В программе генерируется случайное целое число от 0 до 100. 
Пользователь должен его отгадать не более чем за 10 попыток. 
После каждой неудачной попытки должно сообщаться, больше или меньше 
введенное пользователем число, чем то, что загадано. Если за 10 попыток 
число не отгадано, вывести ответ.
"""
import random


secret_number = random.randint(0,100)
attempts = 10
while attempts>0:
    user_number = int(input('Введите число: '))
    if user_number==secret_number:
        print("Победа")
        break
    elif user_number<secret_number:
        print("Секретное число больше")
    else:
        print("Секретное число меньше")
    attempts-=1
    if attempts==0:
        print(f'Ответ: {secret_number}')
    