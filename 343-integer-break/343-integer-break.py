class Solution:
    def integerBreak(self, n: int) -> int:
        
        @lru_cache(None)
        def dp(n,m):
            if n==0 or m==0: return 1 
            if m>n: return dp(n,m-1)
            return max(m*dp(n-m,m),dp(n,m-1))
        
        return dp(n,n-1)