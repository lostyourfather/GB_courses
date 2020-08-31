print(id(100))
a = 111-11
print(id(a))
print(id(11000))
b = 11111-111
print(id(b))


stack = []
stack.append(1)
stack.append(2)
print(stack)
stack.pop()
print(stack)
spam = stack.pop()
print(stack)
stack.append(spam)
print(stack)