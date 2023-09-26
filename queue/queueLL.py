class Node:
    def __init__(self,d):
        self.data= d
        self.next= None
    
class myQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.sz= 0

    def enqueue(self,x):
        temp = Node(x)
        if self.rear is None:
            self.front = temp
        else:
            self.rear.next = temp
        self.rear = temp
        self.sz = self.sz + 1

    def dequeue(self):
        if self.front is None:
            return "empyytyy"
        res = self.front.data
        self.front =self.front.next
        if self.rear is  None:
            self.rear = None
        self.sz = self.sz - 1
        return res

    def getFront(self):
        if self.front is None:
            return "emptyyy"
        return self.front.data
    def getRear(self):
        if self.front is None:
            return "emptyyy"
        return self.rear.data
    def getSize(self):
        return self.sz
    def isEmpty(self):
        return self.getSize() == 0
            

q=myQueue()
q.enqueue(20)
q.enqueue(30)
q.enqueue(50)
print(q.getFront())
print(q.getRear())
print(q.getSize())
print(q.isEmpty())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.getFront())
print(q.getRear())
print(q.getSize())
print(q.isEmpty())
