class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        hs=set(nums)
        res=0
        for i in nums:
            if i-diff in hs and i+diff in hs: res += 1
        return res
        