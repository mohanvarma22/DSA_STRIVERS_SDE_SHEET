#hashing method

# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         d={}
#         for i in range(len(nums)):
#             if nums[i] in d:
#                 d[nums[i]] += 1
#             else:
#                 d[nums[i]] = 1
#         for key,value in d.items():
#             if value >= 2:
#                 return key
#         return False

# we can also solve it using sorting

#mathematical formula method

# def find_duplicate(nums):
#     n=len(nums)-1
#     expected_sum = n*(n+1)//2
#     actual_sum = sum(nums)
#     return actual_sum - expected_sum