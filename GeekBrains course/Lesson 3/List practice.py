import random

def breaking_down():
    rand_list = [random.randint(-100,100) for i in range(100)]
    print(rand_list)

    big_zero = []
    small_zero = []
    for i in rand_list:
        if i>0:
            big_zero.append(i)
        else:
            small_zero.append(i)

    print(big_zero, small_zero)

def insert():
    rand_list = [random.randint(0,100) for i in range(100)]
    number = 10
    place = 4
    rand_list.sort()
    rand_list.append(None)
    print(rand_list)
    i = len(rand_list)-1
    while i>place:
        rand_list[i], rand_list[i-1] = rand_list[i-1], rand_list[i]
        i-=1
    rand_list[place] = number
    print(rand_list)

insert()