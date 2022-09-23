class Solution:
    def numSteps(self, s: str) -> int:
        s=int(s,2)
        c=0
        while s!=1:
            if s%2==0: s = s//2
            else: s += 1
            c += 1
        return c
        