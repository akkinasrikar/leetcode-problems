class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        l=len(nums)
        
        @lru_cache(None)
        def dp(idx,Bool):
            if idx>=l: return 0
            a,b=0,0
            if Bool: a=nums[idx]+dp(idx+1,False)
            else: a=-nums[idx]+dp(idx+1,True)
            b=dp(idx+1,Bool)
            return max(a,b)
        
        return dp(0,True)