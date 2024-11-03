'''optimal solution using kadane's algorithm 
you have to initilaize maxsum and sum with 0 and whenever
sum becomes less than 0 drop the value to zero
else carry the sum'''

from typing import List
def maxSubArray( nums: List[int]) -> int:
    max_sum = nums[0]
    cur_sum = nums[0]
    n=len(nums)
    for i in range(1,n):
        cur_sum=max(nums[i],cur_sum+nums[i])
        if cur_sum>max_sum:
            max_sum=cur_sum
    return max_sum

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("The maximum subarray sum is:", maxSubArray(nums))