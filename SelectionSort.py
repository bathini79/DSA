def getMin(arr,i):
    minimum=arr[i]
    minIndex=i
    for j in range(i,len(arr)):
        if(arr[j]<minimum):
            minIndex=j
            minimum=arr[j]
    return minIndex
def selectionSort(arr,n):
    # Write your code here
    # Do not return anything. Update the given array in-place
    for i in range(n-1):
        minimum=getMin(arr,i)
        arr[i],arr[minimum]=arr[minimum],arr[i]
    return arr
