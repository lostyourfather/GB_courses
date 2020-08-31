'''
Задание
5. Пользователь вводит номер буквы в алфавите.
Определить, какая это буква.
'''
letter = int(input('Введите номер буквы: '))
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(f'Буква под номером {letter} - {alphabet[letter-1]}')