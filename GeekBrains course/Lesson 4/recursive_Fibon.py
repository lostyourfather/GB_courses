import cProfile
import functools


@functools.lru_cache() #хранит в кеше предыдущие результаты выполнения функции
def fib(n):
    if n<2:
        return n
    return (fib(n-1)+fib(n-2))



def test(func):
    lst = [0,1,1,2,3,5,8,13,21,34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')

#cProfile.run('fib(15)')
#test(fib)
#python -m timeit -n 100 -s "import recursive_Fibon" "recursive_Fibon.fib(10)"
#100 loops, best of 5: 31.4 usec per loop
#100 loops, best of 5: 151 nsec per loop