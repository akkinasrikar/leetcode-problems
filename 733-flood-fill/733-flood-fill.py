class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        pixel=image[sr][sc]
        if pixel==newColor: return image
        m,n=len(image),len(image[0])
        def dfs(i,j,p):
            if (i<0 or j<0) or (i>=m or j>=n) or image[i][j]!=p: return
            else:
                image[i][j]=newColor
                dfs(i-1,j,p)
                dfs(i+1,j,p)
                dfs(i,j+1,p)
                dfs(i,j-1,p)
        dfs(sr,sc,pixel)
        return image
        