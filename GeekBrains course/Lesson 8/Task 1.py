'''
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
'''
n = int(input('Введите количество друзей: '))

g = []
for i in range(n):
    g.append([])
    for j in range(n):
        if i>=j:
            g[i].append(0)
        else:
            g[i].append(1)

for k in g:
    print(f'{k}\n')

count = 0
for m in g:
    count += sum(m)

print(count)
