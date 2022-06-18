class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        temp=0
        for i in range(len(nums)):
            temp += nums[i]
            res[i] = temp
        return res