class Solution:
    def longestPalindrome(self, s: str) -> str:
        L=len(s)
        def check(l,r):
            while l>=0 and r<L and s[l]==s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        res=""
        for i in range(L):
            res=max(check(i,i),check(i,i+1),res,key=len)
        return res
                
        