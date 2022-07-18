class Solution:
    def maximumSwap(self, num: int) -> int:
        nums=[int(i) for i in str(num)]
        maxid=len(nums)-1
        a,b=0,0
        for i in range(len(nums)-1,-1,-1):
            if nums[i]>nums[maxid]: maxid=i
            elif nums[i]<nums[maxid]: a,b=i,maxid
        nums[a],nums[b]=nums[b],nums[a]
        return int("".join([str(i) for i in nums]))