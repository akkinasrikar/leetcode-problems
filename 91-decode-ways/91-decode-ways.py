class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s)==0: return 0
        
        @lru_cache(None)
        def dp(s):
            if len(s)>0 and s[0]=="0": return 0
            if len(s)==1 or s=='': return 1
            if int(s[:2])<=26: return dp(s[1:])+dp(s[2:])
            else: return dp(s[1:])
        
        return dp(s)