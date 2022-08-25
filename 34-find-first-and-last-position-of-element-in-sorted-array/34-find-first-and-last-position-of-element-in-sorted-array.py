class Solution:
    def searchRange(self, nums,target):
        
        def findpos(target):
            l,r=0,len(nums)-1
            while l<=r:
                m=(l+r)//2
                if nums[m]<target: l = m+1
                else: r = m-1
            return l
        
        low=findpos(target)
        high=findpos(target+1)-1
        if low<=high: return [low,high]
        return [-1,-1]
            
        