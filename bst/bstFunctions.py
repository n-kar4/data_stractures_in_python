
class node:
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None

def insBST(root, key):
    if root is None:
        return node(key)
    else:
        if root.data == key:
            return root
        elif root.data < key:
            root.right = insBST(root.right, key)
        else:
            root.left = insBST(root.left, key)
    return root
def inOrder(root):
    if root is not None:
        inOrder(root.left)
        print(root.data,end=' ' )
        inOrder(root.right)
def searchBST(root, key):
    if root is None:
        return False
    elif root.data is key:
        return True
    elif key  < root.data:
        return searchBST(root.left, key)
    else:
        return searchBST(root.right, key)
def deleN(root, key):
    if root is None:
        return
    elif root.data > key:
        root.left = deleN(root.left, key)
    elif root.data < key:
        root.right = deleN(root.right, key)
    else:
        if root.right is None:
            return root.left
        if root.left is None:
            return root.right
        curr = root.right
        while curr.left is not None:
            curr = curr.left
        root.data = curr.data
        root.right = deleN(root.right, curr.data)    
    return root

def floorValue(root, key):
    res = None
    while root is not None:
        if key == root.data:
            return root
        elif key > root.data:
            res = root
            root = root.right
        else:
            root = root.left
    return res
def ceilingValue(root, key):
    res = None
    while root is not None:
        if key == root.data:
            return root
        elif key > root.data:
            root = root.right
        else:
            res = root
            root = root.left
    return res


if __name__ == "__main__":
    root = node(50)
    insBST(root,20)
    insBST(root,40)
    insBST(root,30)
    insBST(root,70)
    insBST(root,60)
    insBST(root,10)
    inOrder(root)
    #print(searchBST(root,68))
    #deleN(root,70)
    #deleN(root,50)
    #inOrder(root)
    print("\n",floorValue(root,39).data)
    print(ceilingValue(root,39).data)
