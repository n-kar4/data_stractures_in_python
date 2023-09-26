
def fun(S,N):

        if N<=0:
            return "".join(S)
        else:
            return fun("".join(S),N)
N=17
s='809488245517115276'
S=list(s)
for i in range(len(S)-1):
    while int(S[i])>=int(S[i+1]):
        S[i]=""
        N-=1
print("".join(S))

























# N=int(input())
# for i in range(N,0,-1):
#     s=chr(i+65)
#     for i in range(N-1):
#        s+=chr(i+65)
#        s=s[::-1]
#        s+=chr(i+65)
#     print(s)
    













# N=int(input())
# arr = list(map(int, input().split()))

# res=[]
# arr.sort()
# for i in arr:
#     res.append(i)
#     res=res[::-1]

# for i in res:
#     print(i,end=" ")






















# N=int(input())

# num_1=2
# num_2=8
# a=[2,8]
# while N>2:
#     num_3=2*num_2-num_1
#     a.append(num_3)
#     num_1=num_2
#     num_2=num_3
#     N-=1
# for i in a:
#     print(i)


