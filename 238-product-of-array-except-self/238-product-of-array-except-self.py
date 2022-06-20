class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=1
        Bool=0
        zeros=0
        for i in nums: 
            if i!=0: 
                p=p*i
                continue
            Bool=1  
            zeros += 1
        l=len(nums)
        for i in range(len(nums)):
            if Bool==1 and nums[i]!=0: nums[i]=0
            elif nums[i]==0 and zeros==1: nums[i]=p
            elif nums[i]==0 and zeros!=1: nums[i]=0
            else: nums[i] = int(p/nums[i])
        return nums
        