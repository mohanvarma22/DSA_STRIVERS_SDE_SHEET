class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        left=0
        maxCount=0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            maxCount = max(maxCount,right-left+1)

        return maxCount
            
# Sample usage
solution = Solution()
input_string = "abcabcbb"
result = solution.lengthOfLongestSubstring(input_string)
print(f"The length of the longest substring without repeating characters in '{input_string}' is {result}.")