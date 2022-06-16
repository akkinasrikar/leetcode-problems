class Solution:
    def numTrees(self, n: int) -> int:
        
        @lru_cache(None)
        def dp(n):
            if n==0: return 1
            res=0
            for i in range(n): res += dp(i)*dp(n-i-1)
            return res
        
        return dp(n)
        