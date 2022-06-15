class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxdp=[0]*len(nums)
        mindp=[0]*len(nums)
        maxdp[0]=mindp[0]=nums[0]
        for i in range(1,len(nums)):
            t=nums[i]
            mindp[i]=min(mindp[i-1]*t,maxdp[i-1]*t,t)
            maxdp[i]=max(mindp[i-1]*t,maxdp[i-1]*t,t)
        return max(maxdp)