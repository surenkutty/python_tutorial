
from queue import LifoQueue
stack=LifoQueue(maxsize=4)
stack.put(2)
stack.put(3)
stack.put(4)
print(stack.qsize())
print(stack.full())
stack.get()
print(stack.full())