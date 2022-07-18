class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        r=abs(30*hour-11/2*minutes)
        return min(r,360-r)
        