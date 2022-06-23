class Solution:
    def setZeroes(self, matrix):
        loc=[]
        l=len(matrix[0])
        m=len(matrix)
        for i in range(m):
            for j in range(l):
                if matrix[i][j]==0:
                    loc.append([i,j])
        for r in loc:
            matrix[r[0]]=list([0]*l)
            for i in matrix:
                i[r[1]]=0