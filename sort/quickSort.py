def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]     

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
 
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
 

ar = [10, 7, 8, 9, 1, 5,8,6,4,7,4,541,541,674,9,1,16,46,13,1,4,4,41,634,64,61,3,64,64,64,64,46,4,416,46,46,46,16,1]
n = len(ar)
quickSort(ar, 0, n-1)
print(ar)