class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        def check(s):
            for i,c in enumerate(s):
                if c.swapcase() not in s:
                    return max(check(s[:i]),check(s[i+1:]),key=len)
            return s
        
        return check(s)
        