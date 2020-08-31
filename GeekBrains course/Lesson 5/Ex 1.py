import random
from collections import deque

arr = [random.randint(-100,100) for i in range(10)]
print(arr)
deq = deque()
for item in arr:
    if item>0:
        deq.append(item)
    elif item<0:
        deq.appendleft(item)
print(deq)

with open('ips.txt', 'r') as file:
    last_ten = deque(file,10)
print(last_ten)