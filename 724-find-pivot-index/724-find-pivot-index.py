class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s=sum(nums)
        temp=0
        res=[]
        for i in range(len(nums)-1):
            temp += nums[i]
            if temp == (s-nums[i+1])/2: res.append(i+1)
        if sum(nums[1:])==0: res.append(0)
        if sum(nums[:-1])==0: res.append(len(nums)-1)
        if len(res)>0: return min(res)
        return -1