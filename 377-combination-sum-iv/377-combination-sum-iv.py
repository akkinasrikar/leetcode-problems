class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        @lru_cache(None)
        def dp(target):
            if target==0: return 1
            if target<0: return 0
            count = 0
            for n in nums:
                count += dp(target-n)
            return count
                
        
        return dp(target)