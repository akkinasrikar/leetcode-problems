class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        Bool=False
        for i in range(len(nums)-1):
            if nums[i+1]>=nums[i]: continue
            if Bool: return False
            if i==0 or nums[i+1]>=nums[i-1]:
                nums[i]=nums[i+1]
            else:
                nums[i+1]=nums[i]
            Bool=True
        return True
            
        