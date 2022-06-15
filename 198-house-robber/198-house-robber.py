class Solution:
    def rob(self, nums: List[int]) -> int:
        l=len(nums)
        if l==1: return nums[0]
        if l==0: return 0
        if l==2: return max(nums)
        self.nums=nums
        return self.dp(0,l-1)
        
    @lru_cache(None)
    def dp(self,n,size):
        if n>size: return 0
        return max(self.nums[n]+self.dp(n+2,size),self.dp(n+1,size))
        
        