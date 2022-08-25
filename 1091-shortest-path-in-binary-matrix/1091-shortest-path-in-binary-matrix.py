class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        if grid[0][0] or grid[-1][-1]: return -1
        pos=[[1,0], [-1,0], [0,1], [0,-1], [-1,-1], [1,1], [1,-1], [-1,1]]
        deque=collections.deque([(0,0,1)])
        visited=set()
        visited.add((0,0))
        while deque:
            i,j,d=deque.popleft()
            if i==n-1 and j==n-1: return d
            for p1,p2 in pos:
                x,y=i+p1,j+p2
                if 0<=x<n and 0<=y<n:
                    if (x,y) not in visited and grid[x][y]==0:
                        deque.append((x,y,d+1))
                        visited.add((x,y))
                        grid[x][y]=1
        return -1