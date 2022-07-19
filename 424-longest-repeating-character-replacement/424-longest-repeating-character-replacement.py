class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l=0
        res,mx=0,0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            mx=max(mx,count[s[r]])
            while (r-l+1)-mx>k:
                count[s[l]] -= 1
                l += 1
            res=max(res,(r-l+1))
        return res