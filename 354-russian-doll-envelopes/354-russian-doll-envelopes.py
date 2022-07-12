import bisect
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        env=sorted(envelopes,key=lambda x:(x[0],-x[1]))
        nums=[i for _,i in env]
        def lis(n):
            dp=[]
            for i in range(len(n)):
                idx=bisect.bisect_left(dp,n[i])
                if idx==len(dp):dp.append(n[i])
                else: dp[idx]=n[i]
            return len(dp)
        return lis(nums)