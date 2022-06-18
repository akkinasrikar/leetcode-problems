class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return
        m,n = len(grid),len(grid[0])
        visited = set()
        islands = 0
        
        def bfs(r,c):
            q=collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                rr,cc=q.popleft()
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    r=rr+dr
                    c=cc+dc
                    if (r in range(m) and c in range(n) and (r,c) 
                        not in visited and grid[r][c]=="1"):
                        visited.add((r,c))
                        q.append((r,c))
                
        
        for r in range(m):
            for c in range(n):
                if (r,c) not in visited and grid[r][c]=="1":
                    bfs(r,c)
                    islands += 1
        return islands