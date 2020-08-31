from collections import Counter
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple
from collections import ChainMap
#Counter
'''
a = Counter()
b = Counter('abcdeabfkalsfmasffg')
c = Counter({'red':2, 'black': 5})
d = Counter(cats=5, dogs=7)
print(a,b,c,d, sep='\n')
print(b['z'])
b['z'] = 0
print(b)
print(list(b.elements()))
print(b.most_common(2))
g = Counter(a=4,b=6,c=-2,d=0)
f = Counter(a=1, b=2,c=3,d=-2)
g.subtract(f)
print(g)
print(set(g))
print(dict(g))
g.clear()
print(g)
x = Counter(a=3, b=1)
y = Counter(a=1, b=2)
print(x + y)
print(x - y)
print(x & y)
print(x | y)
z = Counter(a=2, b = -4)
print(+z)
print(-z)
'''
#deque
'''
a = deque()
b = deque('abcdef')
c = deque([1,2,3,4,5])
print(a,b,c,sep='\n')
b = deque('abcdef', maxlen=3)
c = deque([1,2,3,4,5], maxlen=4)
c.clear()
print(b,c,sep='\n')
d = deque([i for i in range(5)], maxlen=7)
d.append(5)
d.appendleft(6)
print(d)
d.extend([7,8,9])
d.extendleft([1,2,3])
print(d)
f = deque([i for i in range(5)], maxlen=7)
x = f.pop()
y = f.popleft()
print(f,x,y, sep='\n')
g = deque([i for i in range(5)], maxlen=7)
print(g.count(2))
print(g.index(3))
g.insert(2,6)
print(g)
g.reverse()
print(g)
g.rotate(3)
print(g)
'''
#defaultdict
'''
a = defaultdict()
print(a)

s = 'asdfghjklwetgdfsjogvbjnjoxcvbnmo'
b = defaultdict(int)
for i in s:
    b[i] += 1
print(b)
list_1 = [('cat', 1), ('dog', 5), ('cat', 2), ('mouse', 1), ('dog', 1)]
c = defaultdict(list)
for k,v in list_1:
    c[k].append(v)
print(c)
list_2 = [('cat', 1), ('dog', 5), ('cat', 2), ('cat', 1), ('dog', 1), ('dog', 5)]
d = defaultdict(set)
for k,v in list_2:
    d[k].add(v)
print(d)
f = defaultdict(lambda: 'unknown')
f.update(rex='dog', tomas='cat')
print(f)
print(f['rex'])
print(f['jerry'])
'''
#OrderedDict
'''
a = {'lion': 7, 'cow': 7, 'cat': 5, 'dog': 2, 'mouse': 4}
new_a = OrderedDict(sorted(a.items(), key=lambda x: x[1]))
print(new_a)

new_a.move_to_end('mouse', last=False)
print(new_a)
new_a.popitem(last=False)
print(new_a)
b = OrderedDict(sorted(a.items(), key = lambda x: len(x[0])))
print(b)
for k in reversed(b):
    print(k, b[k])
'''
#namedtuple
'''
hero_1 = ('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_1[4])
class Person:
    def __init__(self, name, race, health, mana, strenght):
        self.name = name
        self.race = race
        self.health = health
        self.mana = mana
        self.strenght = strenght
hero_2 = Person('Aaz', "Izverg", 100, 0.0, 250)
print(hero_2.mana)
New_Person = namedtuple('New_Person', 'name, race, health, mana, strenght', rename=True)
hero_3 = New_Person('Aaz', "Izverg", 100, 0.0, 250)

Point = namedtuple('Point', 'x,y,z')
p1 = Point(2,z=3,y=4)
print(p1)

t = [5,10,15]
p2 = Point._make(t)
print(p2)

d2 = p2._asdict()
print(d2)

p3 = p2._replace(x=6)
print(p3)

print(p3._fields)

New_Point = namedtuple('New_point', 'x,y,z', defaults=[0,0])
p4 = New_Point(5,7)
print(p4)

print(p4._fields_defaults)

dct = {'x':10, 'y':20, "z":30}
p5 = New_Point(**dct)
print(p5)
'''
#ChainMap
'''
d1 = {'a':2, 'b':4, 'c': 6}
d2 = {'a':10, 'b':20, 'd': 40}
d_map = ChainMap(d1,d2)
print(d_map)
d2['a']=100
print(d_map)
print(d_map['a'])
print(d_map['d'])
x = d_map.new_child({'a':111, 'b': 222, 'c': 333, 'd': 444})
print(x)
print(x.maps[0])
print(x.maps[-1])

print(x.parents)
y = d_map.new_child()
print(y)
print(y['a'])
y['a'] = 1
print(y)
print(list(y))
print(list(y.values()))
'''