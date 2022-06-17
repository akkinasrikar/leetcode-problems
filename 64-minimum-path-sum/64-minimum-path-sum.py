class Solution:
    def minPathSum(self, grid) -> int:
        m,n=len(grid)-1,len(grid[0])-1
        @lru_cache(None)
        def dp(m,n):
            if m<0 or n<0: return 9999999
            if m==0 and n==0: return grid[m][n]
            return grid[m][n]+min(dp(m-1,n),dp(m,n-1))
        return dp(m,n)
        