'''
Задача
1. Выполнить логические побитовые операции
«И», «ИЛИ» и др. над числами 5 и 6. Выполнить
над числом 5 побитовый сдвиг вправо и влево на два знака.
'''

print(f"Операция логическое И между числами 5 и 6 = {5&6}")
print(f"Операция логическое ИЛИ между числами 5 и 6 = {5|6}")
print(f"Операция логическое исключающее ИЛИ между числами 5 и 6 = {5^6}")
print(f"Побитовый сдвиг вправо на знака числа 5 = {5>>2}")
print(f"Побитовый сдвиг влево на знака числа 5 = {5<<2}")