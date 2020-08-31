n = int(input("Введите до какого числа будем искать простые числа: "))
m = [i for i in range(n+1)]
m[1] = 0
for i in range(2,n):
    if m[i]!=0:
        j = i*2
        while j<n:
            m[j] = 0
            j+=i
simple_num = [i for i in m if i!=0]
print(simple_num)