class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m,n=len(grid),len(grid[0])
        islands,c=Counter(),0
        def dfs(i,j,c):
            if not (0<=i<m) or not (0<=j<n) or grid[i][j]!=1: return
            islands[c] += 1 
            grid[i][j]="#"
            dfs(i+1,j,c)
            dfs(i,j+1,c)
            dfs(i-1,j,c)
            dfs(i,j-1,c)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    dfs(i,j,c)
                    c += 1
        return max(list(islands.values())+[0])