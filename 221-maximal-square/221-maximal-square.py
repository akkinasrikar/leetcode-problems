class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m,n=len(matrix),len(matrix[0])
        dp=[[0]*(n+1) for i in range(m+1)]
        
        Max = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=="1":
                    dp[i+1][j+1]=min(dp[i][j+1],dp[i+1][j],dp[i][j])+1
                    Max=max(Max,dp[i+1][j+1])     
        return Max*Max