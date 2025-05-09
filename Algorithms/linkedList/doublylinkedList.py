class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
        self.prev=None
class DoublyLinkedList:
    def __init__(self) -> None:
        self.head=None
    def forward_traversal(self):
        if self.head is None:
            print("Empty")
        else:
            a=self.head
            while a is not None:
                print(a.data,end=" ")
                a=a.next
    def backward_traversal(self):
        if self.head is None:
            print("doublyLinkedList is Empty")
        else:
            a=self.head
            while a.next is not None:
                a=a.next
            while a is not None:
                print(a.data,end=" ")
                a=a.prev
        
link=DoublyLinkedList()

n1=Node(5)
link.head=n1
n2=Node(10)
n2.prev=n1
n1.next=n2
n3=Node(15)
n3.prev=n2
n2.next=n3
n4=Node(20)
n4.prev=n3
n3.next=n4

link.forward_traversal()
print()
link.backward_traversal()