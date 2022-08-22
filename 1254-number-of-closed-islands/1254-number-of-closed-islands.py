class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        m,n=len(grid),len(grid[0])
        
        def dfs(i,j,c):
            if 0<=i<m and 0<=j<n and grid[i][j]==0:          
                grid[i][j]=c
                dfs(i+1,j,c)
                dfs(i,j+1,c)
                dfs(i-1,j,c)
                dfs(i,j-1,c)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0 and (i==0 or j==0 or i==m-1 or j==n-1):
                    dfs(i,j,1)
        res=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    dfs(i,j,1)
                    res += 1
        return res        