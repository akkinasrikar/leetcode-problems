class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l=len(prices)
        
        @lru_cache(None)
        def dp(idx,buy):
            if idx>=l: return 0
            if buy: return max(dp(idx+1,buy),-prices[idx]+dp(idx+1,False))
            else: return max(dp(idx+1,buy),prices[idx]+dp(idx+2,True))
            
        return dp(0,True)