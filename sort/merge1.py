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