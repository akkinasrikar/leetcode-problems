class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        self.matrix=matrix
        x,y=len(matrix),len(matrix[0])
        res=float("inf")
        for i in range(len(matrix[0])):
            res=min(res,self.getminpath(0,i,x,y))
        return res
    @lru_cache(maxsize=None)
    def getminpath(self,i,j,x,y):
        if j<0 or i>x-1 or j>y-1: return float('inf')
        if i==x-1: return self.matrix[i][j]
        return self.matrix[i][j]+min(self.getminpath(i+1,j-1,x,y),self.getminpath(i+1,j,x,y),self.getminpath(i+1,j+1,x,y))
        