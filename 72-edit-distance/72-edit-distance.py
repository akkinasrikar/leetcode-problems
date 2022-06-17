class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @lru_cache(None)
        def dp(a,b):
            if not a and not b: return 0
            if not a: return len(b)
            if not b: return len(a)
            if a[0]==b[0]: return dp(a[1:],b[1:])
            i = 1 + dp(a[1:],b)
            d = 1 + dp(a,b[1:])
            r = 1 + dp(a[1:],b[1:])
            return min(i,d,r)
        
        return dp(word1,word2)
        