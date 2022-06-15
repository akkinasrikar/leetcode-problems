class Solution:
    def rob(self, nums: List[int]) -> int:
        lt=len(nums)
        if lt==1: return nums[0]
        if lt==2: return max(nums)
        self.nums1,self.nums2=nums[1:],nums[:-1]
        return max(self.dp1(0,lt-2),self.dp2(0,lt-2))
    @lru_cache(maxsize=None)
    def dp1(self,n,l):
        if n>l:
            return 0
        return max(self.nums1[n]+self.dp1(n+2,l),self.dp1(n+1,l))
    @lru_cache(maxsize=None)
    def dp2(self,n,l):
        if n>l:
            return 0
        return max(self.nums2[n]+self.dp2(n+2,l),self.dp2(n+1,l))