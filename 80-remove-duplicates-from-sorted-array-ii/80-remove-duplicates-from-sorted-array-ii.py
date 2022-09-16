class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count=0
        prev=None
        pos=0
        last=len(nums)
        for i in range(len(nums)):
            if count==0:
                prev=nums[i]
                count += 1
                nums[pos]=nums[i]
                pos += 1
            elif count==1:
                if prev==nums[i]:
                    count += 1
                    nums[pos]=nums[i]
                    pos += 1
                else:
                    count = 1
                    prev=nums[i]
                    nums[pos]=nums[i]
                    pos += 1
            elif count==2:
                if prev==nums[i]:
                    continue
                else:
                    count = 1
                    prev=nums[i]
                    nums[pos]=nums[i]
                    pos += 1
        return pos
        
            