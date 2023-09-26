import math

class myMinHeap:
    def __init__(self, l=[]):
        self.heap = l
        i=(len(l)-2)//2
        while i>=0:
            self.minHipify(i)
            i=i-1
    
    def printHe(self):
        print(self.heap)
    def parent(self, i):
        return (i-1)//2
    def lChild(self, i):
        return (2*i+1)
    def rChild(self, i):
        return (2*i+2)
    def insertH(self,x):
        self.heap.append(x)
        i = self.heap.index(x)
        while i>0 and self.heap[i] < self.heap[(i-1)//2]:
            self.heap[i],self.heap[(i-1)//2] = self.heap[(i-1)//2],self.heap[i]
            i = self.heap.index(x)
            
    def minHipify(self,i):
        arr = self.heap
        lc = self.lChild(i)
        rc = self.rChild(i)
        smallest = i
        if lc < len(arr) and arr[lc]<arr[smallest]:
            smallest = lc
        if rc < len(arr) and arr[rc]<arr[smallest]:
            smallest = rc
        if smallest != i:
            arr[smallest], arr[i] = arr[i], arr[smallest]
            self.minHipify(smallest)
    def extractMin(self):
        arr = self.heap
        if len(arr) == 0:
            return math.inf
        res = arr[0]
        arr[0] = arr[len(arr)-1]
        arr.pop()
        self.minHipify(0)
        return res

    def decreaseKey(self,i,x):
        arr = self.heap
        arr[i] = x
        while i!=0 and arr[self.parent(i)] > arr[i]:
            arr[self.parent(i)],arr[i] = arr[i],arr[self.parent(i)]
            i=self.parent(i)    
    def deleteKey(self,i):
        if i>len(self.heap):
            return
        else:
            self.decreaseKey(i,-math.inf)
            self.extractMin()




l = [1,5,88,4,7,9,3,2]
heap = myMinHeap(l)
#heap.insertH(10)
#heap.insertH(20)
#heap.insertH(30)
#heap.insertH(38)
#heap.insertH(23)
#heap.insertH(15)
#print(heap.lChild(1))
#print("done")
#heap.printHe()
#heap.decreaseKey(3, 87)
#heap.printHe() 
#heap.deleteKey(3)
heap.printHe()

