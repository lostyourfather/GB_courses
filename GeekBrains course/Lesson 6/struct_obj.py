import sys
import ctypes
import struct
a = 5
x= a
b = 125.54
c = "Hello World!"

print(id(a))
print(sys.getsizeof(a))

print(ctypes.string_at(id(a), sys.getsizeof(a)))
print(struct.unpack('LLLcc', ctypes.string_at(id(a), sys.getsizeof(a))))



print(id(b))
print(sys.getsizeof(b))
z =b
b =122.99
print(ctypes.string_at(id(b), sys.getsizeof(b)))
print(struct.unpack('LLLL', ctypes.string_at(id(b), sys.getsizeof(b))))


print(id(c))
print(sys.getsizeof(c))

print(ctypes.string_at(id(c), sys.getsizeof(c)))
print(struct.unpack('LLLLLLLLLc', ctypes.string_at(id(c), sys.getsizeof(c))))

lst = [1,2,3,4]

print(sys.getsizeof(lst))

print(ctypes.string_at(id(lst), sys.getsizeof(lst)))
print(struct.unpack('LLLLLLLLLLL', ctypes.string_at(id(lst), sys.getsizeof(lst))))