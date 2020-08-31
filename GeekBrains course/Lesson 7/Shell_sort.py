import random

size = 10
lst = [i for i in range(size)]
random.shuffle(lst)
print(lst)

def shell_sort(arr):
    assert len(arr) < 4000, 'List too big. U can use another sort'

    def new_increment(arr):
        inc = [1,4,10,23,57,132,301,701,1750]
        while len(arr) <= inc[-1]:
            inc.pop()
        while len(inc)>0:
            yield inc.pop()
    
    for increment in new_increment(arr):
        for i in range(increment, len(arr)):
            for j in range(i, increment-1, -increment):
                if arr[j-increment] <= arr[j]:
                    break
                arr[j], arr[j-increment] = arr[j-increment], arr[j]

shell_sort(lst)
print(lst)