class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        def kadane(nums):
            a,b=0,-99999999
            for i in range(len(nums)):
                a=a+nums[i]
                if a<nums[i]: a=nums[i]
                if a>b: b=a
            return b
        
        MAX=kadane(nums)
        TOTAL_SUM=0
        for i in range(len(nums)):
            TOTAL_SUM+=nums[i]
            nums[i]=-nums[i]
        MIN=kadane(nums)
        CIRCULAR_SUM=TOTAL_SUM+MIN
        if CIRCULAR_SUM==0: return MAX
        else: return max(CIRCULAR_SUM,MAX)