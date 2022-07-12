class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr = 0
        left = 0
        r = 9999999
        for i in range(len(nums)):
            curr += nums[i]
            while curr>=target:
                r=min(r,i+1-left)
                curr -= nums[left]
                left += 1
        if r==9999999: return 0
        else: return r
                
        