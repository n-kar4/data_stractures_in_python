from collections import deque
import math

def addEdge(arr, u ,v):
    arr[u].append(v)
    arr[v].append(u)
def printEdge(arr):
    for i in arr:
        print(i)
def BFS(arr,s,visited):
    q = deque()
    q.append(s)
    visited.add(s)
    while q:
        s=q.popleft()
        print(s,end=' ')
        for u in arr[s]:
            if u not in visited:
                q.append(u)
                visited.add(u)
def BFSDis(adj):
    visited = {math.inf}
    for u in range(len(adj)):
        if u not in visited:
            BFS(adj, u, visited)


def DFSRec(adj, s, visited):
    visited.add(s)
    print(s, end=' ')
    for u in adj[s]:
        if u not in visited:
            DFSRec(adj, u, visited)
def DFS(adj):
    visited = {math.inf}
    con=0
    for u in range(len(adj)):
        if u not in visited:
            con=con+1
            DFSRec(adj, u, visited)
    print("\n",con)
if __name__=="__main__":
    v = 4
    #arr = [[1,2],[0,3],[0,3],[1,2],[5,6],[4,6],[4,5]]
    #arr = [[1,2],[0,3,4],[0,3],[1,2,4],[1,3]]
    arr = [[1,2],[0,2],[0,1],[3,4],[4,3],[5,6],[6,5]]
    printEdge(arr)
    print("\n")
    DFS(arr)