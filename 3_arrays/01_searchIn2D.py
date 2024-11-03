#1 brute force nested loops
#binary search in 2d

# def binarySearch(arr,target):
#     n=len(arr)
#     low=0
#     high = n-1
#     while low<=high:
#         mid = (low+high)//2
#         if arr[mid] == target:
#             return True
#         elif arr[mid]<target:
#             low=mid+1
#         else:
#             high=mid-1
#     return False

# def search2d(matrix,target):
#     n=len(matrix)
#     m=len(matrix[0])
#     for i in range(n):
#         if matrix[i][0] <= target and target<= matrix[i][m-1]:
#             return binarySearch(matrix[i],target)
#     return False 


'''flattening an array into 2D if we really do it would take
O(n*m) so it would be wasted so we have to make to it 2d 
logically for that we can calculate row = ind / m where m is the no of columns
col=ind%m'''

def search2d(matrix,target):
    n=len(matrix)
    m=len(matrix[0])
    low = 0
    high = (m*n) - 1
    while low<=high:
        mid = (low+high)//2
        row = mid//m
        col=mid%m
        if(matrix[row][col]==target):
            return True
        elif matrix[row][col]<target:
            low=mid+1
        else:
            high=mid-1
    return False


print(search2d([[1,3,5,7],[10,11,16,20],[23,30,34,60]],16))