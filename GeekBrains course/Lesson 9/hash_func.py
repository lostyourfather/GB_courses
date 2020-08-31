import hashlib


h_list = [None] * 26

def my_append(value):
    index  = ord(value[0]) - ord('a')
    h_list[index] = value
    print(h_list)

a = 'apricot'
my_append(a)
b = 'banana'
my_append(b)
c = 'apple'
my_append(c)

def my_index(value):
    letter = 26
    index = 0
    size = 10000
    for i, char in enumerate(value):
        index += (ord(char) - ord('a')+1) * letter ** i
    return index % 10000

print(my_index(a))
print(my_index(b))
print(my_index(c))


print(hashlib.sha1(b'Hello World!').hexdigest())

print(hashlib.sha1(b'secretword' + b'Hello World!').hexdigest())

s = hashlib.sha1(b'Hello World!').hexdigest()

print(s.encode('utf-8'))

print(hashlib.sha1(b'secretword' + bytes(s.encode('utf-8'))).hexdigest())