class Solution:
    def maxProfit(self, p: List[int]) -> int:
        return sum(p[i+1]-p[i] for i in range(len(p)-1) if p[i+1]>p[i])
        