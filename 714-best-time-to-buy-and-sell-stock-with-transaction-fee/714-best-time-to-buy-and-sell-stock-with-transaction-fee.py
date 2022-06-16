class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        size=len(prices)
        if size==1: return 0
        @lru_cache(None)
        def dp(day,buy):
            if day>=size: return 0
            if not buy: return max(dp(day+1,buy),prices[day]+dp(day+1,True)-fee)
            else: return max(dp(day+1,buy),-prices[day]+dp(day+1,False))
        return dp(0,True)