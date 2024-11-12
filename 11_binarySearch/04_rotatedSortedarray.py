'''first edi sorted half oo chudali then aa element aa half lo undemo chudali'''
def rotatedSorted(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid] == target:
            return mid
        if arr[low]<=arr[mid]:
            if arr[low]<=target and arr[mid]>target:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid]<target and target<=arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

arr=[4,5,6,7,0,1,2]
target=0
print(rotatedSorted(arr,target))

