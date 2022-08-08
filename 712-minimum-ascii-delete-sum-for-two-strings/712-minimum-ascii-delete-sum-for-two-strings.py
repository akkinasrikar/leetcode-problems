class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n,m=len(s1),len(s2)
        @lru_cache(None)
        def dp(a,b):
            if a==n or b==m:
                if a==n and b==m: return 0
                if a==n: return sum(ord(s2[i]) for i in range(b,m))
                else: return sum(ord(s1[i]) for i in range(a,n))
            if s1[a]==s2[b]: return dp(a+1,b+1)
            else:
                return min(dp(a+1,b)+ord(s1[a]),dp(a,b+1)+ord(s2[b]))
        return dp(0,0)
        