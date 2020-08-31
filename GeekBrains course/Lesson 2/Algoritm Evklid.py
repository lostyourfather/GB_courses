x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
while y!=0:
    if x>y:
        x=x%y
    else:
        y=y%x
print(x+y)