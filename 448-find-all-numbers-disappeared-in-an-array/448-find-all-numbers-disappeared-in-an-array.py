class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            idx=abs(nums[i])-1
            if nums[idx]>0:
                nums[idx] = -nums[idx]
        res=[i+1 for i in range(len(nums)) if nums[i]>0]
        return res