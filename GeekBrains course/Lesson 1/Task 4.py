'''
Задание
4. Пользователь вводит две буквы. Определить, на каких местах
алфавита они стоят, и сколько между ними находится букв.
'''
letter1 = input('Введите первую букву: ')
letter2 = input('Введите вторую букву: ')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(f'''Номер {letter1}: {alphabet.index(letter1)+1};
Номер {letter2}: {alphabet.index(letter2)+1};
Расстояние между ними: {((alphabet.index(letter2)+1)-(alphabet.index(letter1)+1))-1}''')