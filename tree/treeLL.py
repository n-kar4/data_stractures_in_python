import math
from collections import deque

class node:
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None

class mTree:
    def __init__(self):
        self.root = None


def inOrder(root):
    if root is not None:
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)
def preOrder(root):
    if root is not None:
        print(root.data)
        preOrder(root.left)
        preOrder(root.right)
def postOrder(root):
    if root is not None:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data)
def sizeT(root):
    if root is not None:
        return sizeT(root.left)+sizeT(root.right)+1
    return 0
def maxT(root):
    if root is not None:
        return max(root.data,maxT(root.left),maxT(root.right))
    return -math.inf
def searchK(root,key):
    if root is None:
        return False
    elif root.data is key:
        return True
    elif searchK(root.left,key) is True:
        return True
    else: 
        return searchK(root.right,key)
def heightOfTree(root):
    if root is not None:
        return max(heightOfTree(root.left), heightOfTree(root.right))+1
    return 0

def levelOrder(root):
    if root is None:
        return
    q=deque()
    q.append(root)
    while len(q)>0:
        node = q.popleft()
        print(node.data)
        if root.left.data is not None:
            q.append(node.left)
        if root.right.data is not None:
            q.append(node.right)

        

root = node(30)
root.left = node(20)
root.right = node(40)
root.left.left = node(10)
root.left.right = node(50)
root.right.left = node(20)
root.right.right = node(70)
root.left.right.left = node(90)
root.left.right.right = node(60)
#inOrder(root)
#preOrder(root)
#postOrder(root)
#print(sizeT(root))
#print(maxT(root))
#print(searchK(root,99))
#print(heightOfTree(root))
levelOrder(root)