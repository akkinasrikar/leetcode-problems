# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lo,hi=1,n
        while lo<hi:
            mid=int((lo+hi)/2)
            c=guess(mid)
            if c==0: return mid
            elif c==-1: hi=mid
            else: lo=mid+1
        return lo
                