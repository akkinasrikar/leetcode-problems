class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        zero_position,first_negative,SUM,MAX=-1,-1,0,0
        for i in range(len(nums)):
            if nums[i]<0:
                SUM += 1
                if first_negative==-1: 
                    first_negative = i
            if nums[i]==0:
                SUM=0
                first_negative=-1
                zero_position = i
            else:
                if SUM%2==0: MAX = max(i-zero_position,MAX)
                else: MAX = max(i-first_negative,MAX)
        return MAX
                
        