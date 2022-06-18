class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        t=""
        mx=0
        for i in s:
            if i not in t:
                t += i
                if len(t)>mx: mx=len(t)
            else:
                idx=t.index(i)
                t=t[idx+1:]+i
                if len(t)>mx: mx=len(t)
        return mx
                
        