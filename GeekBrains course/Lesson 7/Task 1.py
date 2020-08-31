import random

def lst_mkr():
    lst = [random.randint(-100,100) for _ in range(10)]
    return lst

def bubble_sort(lst):
    print(lst)
    for i in range(len(lst)-1):
        for j in range(len(lst)-1):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    print(lst)
    return lst

bubble_sort(lst_mkr())