class Solution:
    def maxProductDifference(self, n: List[int]) -> int:
        n.sort()
        return (n[-1]*n[-2])-(n[0]*n[1])