from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cost = 0
        l=0
        for r in range(1,len(prices)):
            cost = prices[r] - prices[l]
            max_profit = max(cost,max_profit)
            if prices[l]>prices[r]:
                l=r
        return max_profit
prices=[1,6,7,2,5,7]
solution=Solution()
print(solution.maxProfit(prices))
