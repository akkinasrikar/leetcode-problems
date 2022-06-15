class Solution:
    def jump(self, nums: List[int]) -> int:
        j,end,far = 0,0,0
        for i in range(len(nums)-1):
            far = max(far,i+nums[i])
            if i==end:
                j += 1
                end = far
        return j