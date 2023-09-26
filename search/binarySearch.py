a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# f=1
# s=0
# e=len(a)-1
# while s<e:
#     mid = (s+e)//2
#     if a[mid]<f:
#         e = mid-1
#     else:
#         s = mid+1
#     if a[mid]==f:
#         print(mid)


# def binary_search(arr, x):
#     low = 0
#     high = len(arr) - 1
#     mid = 0
#     while low <= high:
#         mid = (high + low) // 2
#         # If x is greater, ignore left half
#         if arr[mid] < x:
#             low = mid + 1
#         # If x is smaller, ignore right half
#         elif arr[mid] > x:
#             high = mid - 1
#         # means x is present at mid
#         else:
#             return mid
#     # If we reach here, then the element was not present
#     return -1
 
 
# # Test array
# arr = [ 2, 3, 4, 10, 40 ]
# x = 10
 
# # Function call
# result = binary_search(arr, x)
 
# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in array")







# def bS(a, f):
#     if a[0] == f or a[len(a)//2]==f:
#         print(4)
#     if f<a[len(a)//2]:
#         bS(a[:len(a)//2-1], f)
#     if f>a[len(a)//2]:
#         bS(a[len(a)//2:], f)

# print(bS(a, 39))