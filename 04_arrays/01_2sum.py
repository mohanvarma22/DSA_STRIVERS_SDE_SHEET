#brute force nested loops
#better hashmap
# def twoSum(arr,target):
#     map1={}
#     n=len(arr)
#     for i in range(n):
#         diff =  target - arr[i]
#         if diff in map1:
#             return [map1[diff],i]
        
#         map1[arr[i]] = i
#     return False

#optimal if we only need true or false ans not optimal incase of returning indices

# def twoSum(arr,target):
#     n=len(arr)
#     start=0
#     end=n-1
  
#     arr.sort()
#     while start < end:
#         if arr[start] + arr[end] == target:
#             return [start,end]
#         elif arr[start]+arr[end]<target:
#             start+=1
#         else:
#             end-=1
#     return [-1,-1]


# arr = [2,7,11,15]
# print(twoSum(arr,9))