'''
4. Определить, какое число в массиве встречается чаще всего.
'''

import random as r

numbers = [r.randint(0,5) for i in range(10)]
print(numbers)
num = numbers[0]
max_frq = 1

for i in range(len(numbers)):
    frq = 1
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            frq+=1
    if frq>max_frq:
        max_frq = frq
        num = numbers[i]

print(f'Число {num} встречается {max_frq} раз')