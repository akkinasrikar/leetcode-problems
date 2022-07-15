class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.nums,self.target=nums,target
        return self.dp(len(nums)-1,0)
    
    @lru_cache(maxsize=None)
    def dp(self,i,s):
        if i<0 and s==self.target: return 1
        if i<0: return 0
        return self.dp(i-1,s+self.nums[i])+self.dp(i-1,s+(-self.nums[i]))
        