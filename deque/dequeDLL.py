class Node:
    def __init__(self,d):
        self.data= d
        self.next= None
        self.prev= None

class mDeque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.sz = 0
    
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

    def insFront(self,x):
        temp = Node(x)
        if self.front is None:
            self.front = temp
            self.rear = temp
        else:
            self.front.prev = temp
            temp.next = self.front
        self.front = temp
        self.sz = self.sz + 1
    def insRear(self,x):
        temp = Node(x)
        if self.rear is None:
            self.front = temp
        else:
            self.rear.next = temp
            temp.prev = self.rear
        self.rear = temp
        self.sz = self.sz + 1

    def delRear(self):
        if self.front is None:
            return "empyytyy"
        res = self.front.data
        self.front =self.front.next
        if self.rear is  None:
            self.rear = None
            self.front = None
        self.sz = self.sz - 1
        return res    
    def delRear(self):
        if self.front is None:
            return "Empty"
        res = self.rear.data
        self.rear = self.rear.prev
        if self.rear is None:
            self.rear = None
            self.front = None
        self.sz = self.sz - 1
        return res
        


q=mDeque()
q.insFront(90)
q.insFront(70)
q.insRear(20)
q.insRear(30)
q.insRear(50)
print(q.delRear())
print(q.delRear())
q.insFront(30)
print("          ",q.delRear())
print(q.delRear())
print(q.delRear())
print(q.delRear())
print(q.delRear())
print(q.delRear())

