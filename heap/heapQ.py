import heapq
p=[1,5,88,4,7,9,3,2]
heapq.heapify(p)
print(p)
heapq.heappush(p,2)
print(p)
heapq.heappop(p)
print(p)

print(heapq.heapreplace(p,977))
print(heapq.heappushpop(p,3))
print(p)
print(p)
print(heapq.heapreplace(p,-1))
print(p)