class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res=0
        for n in nums:
            if (n-1) not in nums:
                c = 0
                while True:
                    if (n) in nums: 
                        c += 1
                        n += 1
                    else: break
                res=max(c,res)
        return res
            
        