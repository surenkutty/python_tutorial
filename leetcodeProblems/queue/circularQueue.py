class MyCircularQueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*size
        self.head=self.tail=-1
    def enqueue(self,data):
        if((self.tail+1)%self.k==self.head):
            print("circular queue is Full")
        elif(self.head==-1):
            self.head=0
            self.tail=0
            self.queue[self.tail]=data
        else:
            self.tail=(self.tail+1)%self.k
            self.queue[self.tail]=data
            
    def dequeue(self):  
        if(self.head==-1):
            print("this circular Queue is Empty")
        elif(self.head==self.tail):
            temp=self.queue[self.head]
            self.head=-1
            self.tail=-1
            return temp
        else:
            temp=self.queue[self.head]
            self.head=(self.head+1)%self.k
            return temp
    def printQueue(self):
        if(self.head==-1):
            print("element is the circular Queue is Found")
        elif(self.tail>=self.head):
            for i in range(self.head,self.tail+1):
                print(self.queue[i],end="")
                print()
        else:
            for i in range(self.head,self.k):
                print(self.queue[i],end="")
            for i in range(0,self.tail+1):
                print(self.queue[i],end="")
            print()
obj=MyCircularQueue(5)
obj.enqueue(10)
obj.enqueue(11)
obj.enqueue(12)
obj.enqueue(13)
obj.printQueue()
obj.dequeue()
obj.printQueue()
                
            