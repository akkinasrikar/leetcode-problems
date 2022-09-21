class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s=sum([i for i in nums if i%2==0])
        res=[]
        for i,j in queries:
            temp=nums[j]+i
            a,b=temp%2,nums[j]%2
            if a==0 and b==1: s += temp
            elif a==0 and b==0: s += i
            elif a==1 and b==0: s -= nums[j]
            nums[j] = temp
            res.append(s)
        return res

                
                
        