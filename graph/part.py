from graphLoL import *

def DFSRec(adj, s, visited):
    visited.add(s)
    print(s, end=' ')
    for u in adj[s]:
        if u not in visited:
            DFSRec(adj, u, visited)

def DFS(adj):
    visited = {math.inf}
    con=0
    for u in range(len(adj)-1):
        if u not in visited:
            con=con+1
            DFSRec(adj, u, visited)
    print("\n",con)

arr = [[1,2],[0,2],[0,1],[3,4],[4,6],[5,6],[7,5]]
print(DFS(arr))