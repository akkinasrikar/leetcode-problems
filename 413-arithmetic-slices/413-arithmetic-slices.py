class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        l=len(nums)
        res=[0]*l
        for i in range(2,l):
            if nums[i-1]-nums[i]==nums[i-2]-nums[i-1]:
                res[i] = 1+res[i-1]
        #print(res,sum(res))
        return sum(res)
        