n = int(input('Введите десятичное число: '))
binary = ''
while n>0:
    binary = str(n%2) + binary
    n = n//2
print(binary)