class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l=len(nums)
        s=sum(list(range(0,l+1)))
        #print(s,l)
        return s-sum(nums)
        
        