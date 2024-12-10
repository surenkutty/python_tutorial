class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.pointer=None
class LinkedList:
    def __init__(self) -> None:
        self.head=None
    def Add(self):
        if self.head is None:
            print("linked List Is Empty")
        else:
            a=self.head
            while a is not None:
                print(a.data,end=" ")
                a=a.pointer
    def Add_at_begin(self,data):
        print()
        nb=Node(data)
        nb.pointer=self.head
        self.head=nb
    def Add_at_end(self,data):
        ne=Node(data)
        a=self.head
        while a.pointer is not None:
            # print(a.pointer,end="")
            a=a.pointer
        a.pointer=ne
    def Add_specified_position(self,position,data):
        nib=Node(data)
        a=self.head
        for i in range(1,position-1):
            a=a.pointer
        nib.pointer=a.pointer
        a.pointer=nib
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
    def position_deletion(self,position):
        print()
        prev=self.head
        a=self.head.pointer
        for i in range(1,position-1):
            a=a.pointer
            prev=prev.pointer
        prev.pointer=a.pointer
        a.pointer=None
        
        
        
                
link=LinkedList()

n1=Node(5)
link.head=n1
n2=Node(10)
n1.pointer=n2
n3=Node(15)
n2.pointer=n3
n4=Node(20)
n3.pointer=n4

link.Add()
link.Add_at_begin(1)
link.Add_at_end(25)
link.Add_specified_position(6,8)
link.Add()
link.deletion_begin()
link.Add()
link.deletion_end()
link.Add()
link.position_deletion(2)
link.Add()


        