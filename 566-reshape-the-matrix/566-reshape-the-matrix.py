class Solution:
    def matrixReshape(self,mat,r,c) :
        m,n=len(mat),len(mat[0])
        if m*n!=r*c: return mat
        temp=[]
        for i in mat: temp += i
        res=[]
        for i in range(r):
            res.append(temp[i*c:i*c+c])
        return res
        