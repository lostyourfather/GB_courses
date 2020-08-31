import random

def lst_mkr():
    lst = [random.randint(0,50) for _ in range(10)]
    return lst

def merge_sort(lst):
    if len(lst)<=1:
        return lst
    mid = len(lst)//2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left)>0 and len(right)>0:
        if right[0]<=left[0]:
            result.append(right[0])
            right = right[1:]
        else:
            result.append(left[0])
            left = left[1:]
    if len(left)>0:
        result += left
    if len(right)>0:
        result += right
    return result

srt_lst = lst_mkr()
end_lst = merge_sort(srt_lst)
print(srt_lst)
print(end_lst)
    