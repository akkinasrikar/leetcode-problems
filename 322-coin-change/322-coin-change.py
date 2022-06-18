class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        @lru_cache(None)
        def dp(amount):
            if amount==0 : return 0
            if amount<0: return float("inf")
            return min(1+dp(amount-coin) for coin in coins)
        
        res=dp(amount)
        return [-1,res][res!=float("inf")]