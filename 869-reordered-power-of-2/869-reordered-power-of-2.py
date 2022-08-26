class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        a=Counter(str(n))
        for i in range(30):
            if Counter(str(1<<i))==a: return True
        return False