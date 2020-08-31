import random
from collections import namedtuple
from operator import attrgetter
size = 10
lst = [i for i in range(size)]
random.shuffle(lst)
print(lst)

def revers(arr):
    for i in range(len(arr)//2):
        arr[i], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]
revers(lst)
print(lst)
lst.reverse()
print(lst)
lst.sort(reverse=True)
print(lst)

t = tuple(random.randint(1,100) for _ in range(size))
print(t)
t = tuple(sorted(t, reverse = True))
print(t)

Person = namedtuple('Person', 'name age')
p1 = Person('Artem', 22)
p2 = Person('Tany', 20)
p3 = Person('Rinat', 21)

people = [p1,p2,p3]
print(people)
#result = sorted(people, key = lambda person: person.age)
result = sorted(people, key = attrgetter('age'))
print(result)