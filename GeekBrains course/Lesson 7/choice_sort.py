import random

size = 10
lst = [i for i in range(size)]
random.shuffle(lst)
print(lst)

def choice_sort(arr):
    for i in range(len(arr)):
        ind_min = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[ind_min]:
                ind_min=j
        arr[ind_min], arr[i] = arr[i], arr[ind_min]
choice_sort(lst)
print(lst)