from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        end1=m-1
        end2=n-1
        insert_pos = m+n-1
        while end1>=0 and end2>=0:
            if nums1[end1]>nums2[end2]:
                nums1[insert_pos] = nums1[end1]
                end1 -= 1
            else:
                nums1[insert_pos] = nums2[end2]
                end2 -= 1
            insert_pos-=1
        
        while end2>=0:
            nums1[insert_pos] = nums2[end2]
            end2-=1
            insert_pos-=1

        return nums1
    
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
solution=Solution()
print(solution.merge(nums1,m,nums2,n))