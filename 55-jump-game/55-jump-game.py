class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)-1
        goal = l
        for i in range(l,-1,-1):
            if i+nums[i]>=goal:
                goal = i
        return [False,True][goal==0]
        