import random

size = 10
lst = [i for i in range(size)]
random.shuffle(lst)
print(lst)

for j in range(len(lst)-1):
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
print(lst)

