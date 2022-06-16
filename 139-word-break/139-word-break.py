class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        @lru_cache(None)
        def dp(s):
            if s=="": return True
            for i in wordDict:
                try:
                    idx=s.index(i)
                    if idx==0:
                        suffix=s[len(i):]
                        if dp(suffix): return True
                except:
                    continue
            return False
        
        return dp(s)