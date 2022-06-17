class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s,t=list(s),list(t)
        for i in t:
            try:
                if s[0]==i: s.pop(0)
            except:
                continue
        return True if len(s)==0 else False
        