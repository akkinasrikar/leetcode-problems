class Solution:
    def minimumSum(self, num: int) -> int:
        num=list(str(num))
        num.sort()
        a=num[0]+num[-1]
        b=num[1]+num[-2]
        return int(a)+int(b)
        