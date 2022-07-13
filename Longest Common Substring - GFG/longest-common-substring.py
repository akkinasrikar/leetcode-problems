#User function Template for python3

class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        # code here
        Max=0
        dp=[[0]*(m+1) for i in range(n+1)]
        for i in range(n):
            for j in range(m):
                if S1[i]==S2[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                    Max=max(Max,dp[i+1][j+1])
        return Max
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n,m = input().strip().split(" ")
        n,m = int(n), int(m)
        S1 = input().strip()
        S2 = input().strip()
        
        
        ob=Solution()
        print(ob.longestCommonSubstr(S1, S2, n, m))
# } Driver Code Ends