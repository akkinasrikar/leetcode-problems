class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeropos=[]
        for i in range(len(nums)):
            if nums[i]==0:
                zeropos.append(i)
            else:
                if zeropos:
                    p=zeropos.pop(0)
                    nums[p]=nums[i]
                    nums[i]=0
                    zeropos.append(i)
                else:
                    continue
                    
                
        