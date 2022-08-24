class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r,c=len(heights),len(heights[0])
        pac,alt=set(),set()
        
        def dfs(x,y,visit,prev):
            if (x<0 or y<0 or x==r or y==c) or ((x,y) in visit) or (heights[x][y]<prev): return 
            visit.add((x,y))
            prev=heights[x][y]
            dfs(x+1,y,visit,prev)
            dfs(x-1,y,visit,prev)
            dfs(x,y+1,visit,prev)
            dfs(x,y-1,visit,prev)
        
        for R in range(r):
            dfs(R,0,pac,heights[R][0])
            dfs(R,c-1,alt,heights[R][c-1])
            
        for C in range(c):
            dfs(0,C,pac,heights[0][C])
            dfs(r-1,C,alt,heights[r-1][C])
        
        res=[]
        for i in range(r):
            for j in range(c):
                if (i,j) in pac and (i,j) in alt:
                    res.append([i,j])
        return res
        
            
        