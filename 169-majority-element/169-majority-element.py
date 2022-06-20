class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major=nums[0]
        counter=1
        for i in range(1,len(nums)):
            if counter==0:
                major=nums[i]
                counter += 1
            elif major==nums[i]:
                counter += 1
            else:
                counter -= 1
        return major
        