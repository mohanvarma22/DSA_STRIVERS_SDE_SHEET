from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans=[]
        n=len(intervals)
        for i in range(n):
            if not ans or intervals[i][0]>ans[-1][1]:
                ans.append(intervals[i])
            else:
                ans[-1][1] = max(ans[-1][1],intervals[i][1])
        return ans
intervals = [[1,3],[2,6],[8,10],[15,18]]
solution = Solution()
print(solution.merge(intervals))