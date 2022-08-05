class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        sq,nsq,res=0,0,0
        for i in nums:
            sq=max(i*i,sq+i,nsq+i*i)
            nsq=max(i,nsq+i)
            res=max(res,sq,nsq)
        return res
            
        