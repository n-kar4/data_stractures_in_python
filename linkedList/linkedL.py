class node:
    def __init__(self, x):
        self.key=x
        self.next=None
    
def printL(head):
    curr=head
    while curr is not None:
        print(curr.key,end=" ")
        curr=curr.next
    print("\n")

def searchL(head, i):
    pos=1
    curr=head
    while curr is not None:
        if curr.key== i:
            return pos
        curr=curr.next
        pos=pos+1

def insertB(head,key):
    temp=node(key)
    temp.next=head
    return temp

def insertE(head,key):
    temp=node(key)
    curr=head
    while curr.next is not None:
        curr=curr.next
    curr.next=temp
    return head

def insertP(head,key,p):
    temp=node(key)
    if p==1:
        temp=node(key)
        temp.next=head
        return temp

    curr=head
    for i in range(p-2):
        curr=curr.next
        if curr is None:
            return head
    temp.next=curr.next
    curr.next=temp
    return head
 
def delp(head,key):
    if head.key==key:
        return head.next
    prev = None
    curr=head
    while curr is not None:
        if curr.key==key:
            prev.next=curr.next
        prev=curr
        curr=curr.next
    return head           

def revL(head):
    prev=None
    curr=head
    while curr is not None:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    return prev

head=node(10)
head.next=node(20)
head.next.next=node(30)
printL(head)

# print("found at ",searchL(head, 20))
# head=insertB(head, 50)
# printL(head)
head=insertE(head,70)
printL(head)
# head=insertP(head,80,3)
# printL(head)
# head=delp(head,50)
# printL(head)
# head=revL(head)
# printL(head)