from collections import deque

stack=deque()
stack.append('x')
stack.append("y")
print(stack)
stack.pop()     #pop is remove last element
print(stack)