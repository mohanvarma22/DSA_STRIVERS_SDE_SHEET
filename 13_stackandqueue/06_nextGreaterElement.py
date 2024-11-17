#Brute Force nested loops
#stack implementation
'''reverse traversal chestu greater elements anni store
cheskuntu if stack lo top element greater undakpote
greater element oche varaku pop chesi greater element return 
cheyali'''
def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        
        # Find next greater element for each number in nums2
        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()
            
            next_greater[num] = stack[-1] if stack else -1
            stack.append(num)
        
        # Map the result for nums1
        return [next_greater[num] for num in nums1]