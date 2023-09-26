def sellSort(l):
    for i in range(len(l)-1):
        min=i
        for j in range(i+1,len(l)):
            if l[j] < l[min]:
                l[i],l[j]=l[j],l[i]
        
    return l
    
l=[4,5,2,3,8,5,1,6,6]
print(sellSort(l))

