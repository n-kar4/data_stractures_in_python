def merge(l, low, mid, high):
    i=low
    j=mid+1
    res=[]  
    while i<=mid and j<=high:
        if l[i]<l[j]:
            res.append(l[i])
            i=i+1
        else:
            res.append(l[j])
            j=j+1
    while i<=mid:
        res.append(l[i])
        i=i+1
    while j<=high:
        res.append(l[j])
        j=j+1
    return res

def mergeSort(l, left, right):
    if right> left:
        m = (left+right)//2
        mergeSort(l, left, m)
        mergeSort(l, m+1, right)
        return merge(l, left, m, right)



l=[4,5,2,3,8,5,1,6,6]
l= mergeSort(l,0,len(l)-1)
print(l)