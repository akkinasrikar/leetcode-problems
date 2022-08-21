class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a,b=float("-inf"),float("-inf")
        for i in nums:
            if a<i: 
                b=max(b,a)
                a=i
            elif b<i: b=max(i,b)
        return (a-1)*(b-1)