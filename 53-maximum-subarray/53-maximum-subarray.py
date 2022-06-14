class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a,b=0,-99999
        for i in range(len(nums)):
            a=a+nums[i]
            if a<nums[i]: a=nums[i]
            if b<a: b=a
        return b
        