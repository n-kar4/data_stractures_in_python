class Node:
    def __init__(self,d):
        self.data = d
        self.next = None

class myStack:
    def __init__(self):
        self.head=None
        self.s=0
    def push(self,x):
        temp=Node(x)
        temp.next = self.head
        self.head=temp
        self.s=self.s+1
    def peek(self):
        if self.head is None:
            return "Empty"
        return self.head.data
    def pop(self):
        if self.head is None:
            return "Underflowwww"
        self.head=self.head.next
        self.s=self.s-1

s=myStack()
s.push(10)
s.push(22)
print(s.peek())
s.pop()
print(s.peek())
s.pop()
print(s.peek())
s.pop()
print(s.peek())
