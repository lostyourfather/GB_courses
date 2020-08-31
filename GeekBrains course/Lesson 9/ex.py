res = 0
def test_func():
    global res
    res=456+100000
    if res<21401:
        test_func()
    return res

print(test_func())