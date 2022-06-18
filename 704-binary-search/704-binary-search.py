class Solution:
    def search(self, nums: List[int], target: int) -> int:
        self.n=nums
        return self.bn(0,len(nums)-1,target)
    def bn(self,l,r,t):
        if r>=l:
            m=l+(r-l)//2
            if self.n[m]==t: return m
            elif self.n[m]>t: return self.bn(l,m-1,t)
            else: return self.bn(m+1,r,t)
        else: return -1
        