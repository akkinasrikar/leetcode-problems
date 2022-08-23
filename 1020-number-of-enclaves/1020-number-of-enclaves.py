class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        m,n=len(grid),len(grid[0])
        def dfs(i,j):
            if (not 0<=i<m) or (not 0<=j<n) or grid[i][j]==0:
                return
            
            grid[i][j]=0 
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i==0 or i==m-1 or j==0 or j==n-1):
                    dfs(i,j)

        return sum([sum(i) for i in grid])

            
        