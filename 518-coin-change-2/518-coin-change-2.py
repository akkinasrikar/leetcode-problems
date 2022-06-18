class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @lru_cache(None)
        def dp(amount,size):
            if size==0: return 0
            if amount==0: return 1
            if coins[size-1]>amount: return dp(amount,size-1)
            return dp(amount-coins[size-1],size)+dp(amount,size-1)
        
        return dp(amount,len(coins))