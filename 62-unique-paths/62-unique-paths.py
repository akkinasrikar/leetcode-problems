from functools import lru_cache
class Solution:
    def uniquePaths(self, m,n):
        
        @lru_cache(None)
        def dp(m,n):
            if m==1 and n==1: return 1
            if m<=0 or n<=0: return 0
            return dp(m-1,n)+dp(m,n-1)
    
        return dp(m,n)
        