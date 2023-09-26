x=[14,9,5,9,3,2]

global T,tf,summ
T=0
summ=sum(x)
tf=False
def subsetsUtil(A, subset, index):
    global T,tf
    if summ-sum(subset)==sum(subset):
        tf=True
        print(subset)
        throw
    # print(subset,index)
    for i in range(index, len(A)):  
        T+=1
        subsetsUtil(A, subset+[A[i]], i + 1)
    

print(subsetsUtil(x, [], 0),T,tf)
     
