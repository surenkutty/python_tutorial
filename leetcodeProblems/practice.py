class Node:
    def __init__(self,data):
        self.data=data 
        self.pointer=None

class LinkedList:
    def __init__(self):
        self.head=None
    def traversal(self):
        if self.head is None:
            print("singlyLinked List is Empty")
        else:
            a=self.head
            while a is not None:
                print(a.data,end=" ")
                a=a.pointer
sll=LinkedList()
n1=Node(10)
sll.head=n1
n2=Node(15)
n1.pointer=n2

n3=Node(20)
n2.pointer=n3
n4=Node(25)
n3.pointer=n4
sll.traversal()
    