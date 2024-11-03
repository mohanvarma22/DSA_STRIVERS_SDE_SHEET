from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=0
        high=len(nums)-1
        i=0
        while i<=high:
            if nums[i] == 0:
                nums[low],nums[i]=nums[i],nums[low]
                i+=1
                low+=1
            elif nums[i] == 2:
                nums[high],nums[i]=nums[i],nums[high]
                high-=1
                i+=1
            else:
                i+=1
        return nums
nums= [0,1,1,2,0,1]
solution = Solution()
solution.sortColors(nums)
print(nums)