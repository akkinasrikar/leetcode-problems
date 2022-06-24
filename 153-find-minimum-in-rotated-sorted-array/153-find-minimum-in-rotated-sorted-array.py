class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1
        while h>l:
            m=l+(h-l)//2
            if nums[m]>nums[h]: l = m+1
            else: h = m
        return nums[l]
        