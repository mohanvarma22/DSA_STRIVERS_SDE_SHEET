#main formula summation of min(leftMax,rightMax)-arr[i]

# prefixMax and suffixMax kanukkovali

#brute force solution using extra space(both prefix and suffix)

# def trap(arr):
#     n=len(arr)
#     prefix=[0]*n
#     suffix=[0]*n
#     prefix[0]=arr[0]
#     waterTrapped = 0
#     for i in range(1,n):
#         prefix[i] = max(prefix[i-1],arr[i])
#     suffix[n-1]=arr[n-1]
#     for i in range(n-2,-1,-1):
#         suffix[i] = max(suffix[i+1], arr[i])#ee steps deggara mistake chesa dont repeat it
#     for i in range(n):
#         waterTrapped += min(suffix[i],prefix[i]) - arr[i]
#     return waterTrapped


'''using only suffix
class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        suffix=[0]*n
        waterTrapped = 0
        suffix[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            suffix[i] = max(suffix[i+1],height[i])
        maxEl = 0
        for i in range(n):
            maxEl = max(maxEl,height[i])
            waterTrapped += min(maxEl,suffix[i]) - height[i]
        return waterTrapped'''

def trap(arr):
    n=len(arr)
    left=0
    right=n-1
    leftMax=0
    rightMax=0
    res=0
    while left<=right:
        if arr[left] <= arr[right]:
            if arr[left]>=leftMax:
                leftMax = arr[left]
            else:
                res+=leftMax - arr[left]
            left+=1
        else:
            if arr[right] >= rightMax:
                rightMax=arr[right]
            else:
                res+=rightMax - arr[right]
            right -= 1
    return res


    
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(arr))