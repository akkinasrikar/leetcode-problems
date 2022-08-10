class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        res=0
        l,m=0,1
        while l<len(nums)-2:
            while m<len(nums)-1:
                diff1=nums[m]-nums[l]
                if diff1==diff:
                    r=m+1
                    while r<len(nums):
                        diff2=nums[r]-nums[m]
                        if diff2==diff1:
                            #print(l,m,r,nums[l],nums[m],nums[r])
                            res += 1
                        if diff2<diff1: r += 1
                        else: break
                m += 1
            l += 1
            m = l+1
        return res
            
            
        