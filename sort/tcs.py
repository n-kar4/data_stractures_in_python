

a=[6,3,8,2,4,9,1,5,7]
# a=[1, 2, 3, 4, 5, 6, 7, 8, 9,12]
count=0

#  BUBBLE
# for i in range(len(a)-1):
#     for j in range(len(a)-i-1):
#         count +=1
#         if a[j]>=a[j+1]:
#             a[j],a[j+1] = a[j+1],a[j] 

#  SELECTION
# for i in range(len(a)):
#     temp=i
#     for j in range(i+1, len(a)):
#         count +=1
#         if a[j] < a[temp]:
#             temp = j
#     a[i],a[temp] = a[temp], a[i]
#     print(a[i],a[temp])        

for i in range(1,len(a)):
    curr=a[i]
    j=i-1
    while j>=0 and curr<a[j]:
        a[j+1]=a[j]
        j-=1
    a[j+1] = curr


print(a, count)