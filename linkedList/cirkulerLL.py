class node:
    def __init__(self, x):
        self.key=x
        self.next=None

def printCL(head):
    if head.next is None:
        print(head.key)
    print(head.key, end=" ")
    curr=head.next
    while curr is not head:
        print(curr.key, end=" ")
        curr=curr.next





head=node(10)
head.next=node(20)
head.next.next=node(30)
head.next.next.next=head
printCL(head)