class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        
        def dfs(r,c):
            if not 0<=r<m or not 0<=c<n or grid[r][c]==0: return 0
            directions = [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
            temp = grid[r][c]
            grid[r][c]=0
            res=0
            for i in directions:
                a,b=i
                res=max(res,dfs(a,b))
            grid[r][c]=temp
            return grid[r][c]+res
        
        final=0
        for i in range(m):
            for j in range(n):
                final=max(final,dfs(i,j))
        return final