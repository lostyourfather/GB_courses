import random

size = 10
lst = [i for i in range(size)]
random.shuffle(lst)
print(lst)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    s_arr = []
    m_arr = []
    l_arr = []
    for i in arr:
        if i<pivot:
            s_arr.append(i)
        elif i==pivot:
            m_arr.append(i)
        elif i>pivot:
            l_arr.append(i)
        else:
            raise Exception('Error')
    return quick_sort(s_arr) + m_arr + quick_sort(l_arr)
new_lst = quick_sort(lst)
#print(new_lst)
def quick_sort_no_mem(arr,fst,lst):
    if fst >= lst:
        return
    pivot = arr[random.randint(fst,lst)]
    i,j = fst, lst

    while i<=j:

        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <=j:
            arr[i], arr[j] = arr[j], arr[i]
            i,j = i+1, j-1

    quick_sort_no_mem(arr,fst,j)
    quick_sort_no_mem(arr,i,lst)

quick_sort_no_mem(lst,0,len(lst)-1)
print(lst)