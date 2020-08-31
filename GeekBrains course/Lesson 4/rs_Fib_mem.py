import cProfile
def test(func):
    lst = [0,1,1,2,3,5,8,13,21,34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')

def fib_dict(n):
    fib_d = {0:0, 1:1}
    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]
        fib_d[n] = _fib_dict(n-2) + _fib_dict(n-1)
        return fib_d[n]
    return _fib_dict(n)

def fib_list(n):
    fib_l = [None] *1000
    fib_l[:2] = [0,1]
    def _fib_list(n):
        if fib_l[n] is None:
            fib_l[n] = _fib_list(n-2) + _fib_list(n-1)
            return fib_l[n]
        return fib_l[n]
    return _fib_list(n)
#test(fib_list)
#100 loops, best of 5: 5.53 usec per loop
#cProfile.run('fib_dict(10)')
#         23 function calls (5 primitive calls) in 0.000 seconds
#     19/1    0.000    0.000    0.000    0.000 rs_Fib_mem.py:10(_fib_dict)

#100 loops, best of 5: 9.03 usec per loop
#cProfile.run('fib_list(10)')
#         23 function calls (5 primitive calls) in 0.000 seconds
#     19/1    0.000    0.000    0.000    0.000 rs_Fib_mem.py:20(_fib_list)