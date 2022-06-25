from collections import Counter
class Solution:
    def countBits(self, n):
        return [Counter(bin(i))["1"] for i in range(n+1)]    