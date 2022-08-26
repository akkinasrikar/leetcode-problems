class Solution:
    def arrangeCoins(self, n: int) -> int:
        r=1
        c=1
        res=0
        while c<=n:
            n -= r
            res += 1
            r += 1
            c += 1
        return res
        