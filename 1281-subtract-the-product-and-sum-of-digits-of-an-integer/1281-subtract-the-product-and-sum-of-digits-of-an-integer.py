class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s,p=0,1
        while n:
            t=n%10
            s += t
            p *=t
            n = n//10
        return p-s
        