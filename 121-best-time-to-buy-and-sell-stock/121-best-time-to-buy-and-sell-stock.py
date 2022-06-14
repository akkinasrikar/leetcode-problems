class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        best = prices[0]
        for i in prices:
            if i-best>profit: profit = i-best
            if i<best: best = i
        return profit
            