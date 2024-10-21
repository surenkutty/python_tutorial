# put     ->insert the Queue
# maxsize ->To initialize the MaxSizeValue
#qsize   ->To Check the queueSize
#full()  ->To check its full or its space or empty
#get     -> to Remove or delete the Last Value

from queue import LifoQueue

stack=LifoQueue(maxsize=3)
stack.put(2)
stack.put(3)
stack.put(4)
print(stack.qsize())
print(stack.full())
print(stack.get())
print(stack.full())