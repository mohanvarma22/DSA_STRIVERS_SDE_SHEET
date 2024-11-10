from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n=len(g)
        m=len(s)
        i=0
        j=0
        count=0
        while i<n and j<m:
            if g[i]<=s[j]:
                count+=1
                i+=1
                j+=1
            else:
                j+=1
        return count

if __name__ == "__main__" :
    g=[1,2,3]
    s=[1,1]
    solution = Solution()
    
    # Call the method using the class instance
    result = solution.findContentChildren(g, s)
    
    # Output the result
    print(result) 