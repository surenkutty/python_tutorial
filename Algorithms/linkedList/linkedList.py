# linkedList
'''
data+ nextpointer  -> data+poiner ->indexdat+Null
   nodevalue       node prev value      node value
'''

class Node:
    
    def __init__(self,data) -> None:
        self.data=data
        self.pointer=None
    '''
    def __str__(self) -> str:
        return node1
    '''
        
head=Node(1)
node2=Node(2)
node3=Node(3)

head.pointer=node2
node2.pointer=node3
'''
print(head.data)
print(head.pointer)  #head
print(node2)
print(node2.data)
print(node2.pointer) #middle
print(node3)
print(node3.data)
print(node3.pointer) #end
'''
current=head
while (current is not None):
    print(current.data)
    current=current.pointer
print(head.data)
print(current)

 