class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dvs,dvd=abs(divisor),abs(dividend)
        res=0
        while dvd>=dvs:
            temp=dvs
            mul=1
            while dvd>=temp:
                dvd -= temp
                res += mul
                mul += mul
                temp += temp
        if (divisor<0 and dividend>=0) or (dividend<0 and divisor>=0):
            res = -1*res
        return min(2147483647,max(-2147483648,res))
                
                