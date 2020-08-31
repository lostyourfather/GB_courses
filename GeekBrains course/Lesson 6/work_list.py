lst = []
lst.append(1)
lst.extend([2,3,4])
print(lst)
lst.insert(1,5)
print(lst)
def list_in_py():
    allocated = 0
    for newsize in range(100):
        if allocated<newsize:
            new_allocated = (newsize>>3) + (3 if newsize<9 else 6)
            allocated = newsize + new_allocated
        print(newsize, allocated)
list_in_py()
last = lst.pop()
print(lst,last)
last = lst.pop()
print(lst,last)
lst.remove(5)
print(lst)