import random

size = 10
lst = [i for i in range(size)]
random.shuffle(lst)
print(lst) 

def insertion_sort(arr):
    for i in range(1,len(arr)):
        spam = arr[i]
        j = i
        while arr[j-1] > spam and j > 0:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = spam
insertion_sort(lst)
print(lst)