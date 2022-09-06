class Solution:
    def countOdds(self, low: int, high: int) -> int:
        res=(high-low)//2
        if low%2==0: return (high-low+1)//2
        else: return res+1
        