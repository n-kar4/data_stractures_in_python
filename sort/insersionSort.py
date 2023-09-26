import insersionSort

def inse(l):
    for i in range(1,len(l)):
        t=l[i]
        j=i-1
        while j>=0 and t<l[j]:
            l[j+1]=l[j]
            j-=1
        l[j+1]=t
        
    return l

if __name__=="__main__":
    l=[4,5,2,3,8,5,100,6]
    print(inse(l))
    