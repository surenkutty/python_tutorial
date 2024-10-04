class Node:
    def __init__(self,data) -> None:
        self.data=data 
        self.pointer=None
class LinkedList:
    def __init__(self) -> None:
        head=None
    def traversal(self):
        if self.head is  None:
            print("empty")
        else:
            a=self.head
            while a is not None:
                print(a.data,end=" ")
                a=a.pointer
    def insert_begin(self,data):
        print()
        nb=Node(data)
        nb.pointer=self.head
        self.head=nb
    def insert_end(self,data):
        print()
        ne=Node(data)
        a=self.head
        while a.pointer is not None:
            a=a.pointer
        a.pointer=ne
    def position(self,positon,data):
        print()
        np=Node(data)
        a=self.head
        for i in range(1,positon-1):
            a=a.pointer
        np.pointer=a.pointer  #replace the next node
        a.pointer=np
    def deletion_begin(self):
        print()
        a=self.head
        self.head=a.pointer
        a.pointer=None
    def deletion_end(self):
        print()
        prev=self.head
        a=self.head.pointer
        while a.pointer is not None:
            a=a.pointer
            prev=prev.pointer
        prev.pointer=None
    def position_deletion(self,positon):
        print()
        prev=self.head
        a=self.head.pointer
        for i in range(1,positon-1):
            a=a.pointer
            prev=prev.pointer
        prev.pointer=a.pointer
        a.pointer=None
      
link=LinkedList()
n1=Node(10)
link.head=n1
n2=Node(20)
n1.pointer=n2
n3=Node(30)
n2.pointer=n3
n4=Node(40)
n3.pointer=n4

link.traversal()
link.insert_begin(90)
link.traversal()
link.insert_end(100)
link.traversal()
link.position(4,35)
link.traversal()
link.deletion_begin()
link.traversal()
link.deletion_end()
link.traversal()
link.position_deletion(2)
link.traversal()