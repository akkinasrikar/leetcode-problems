class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        integral_image = [[0 for i in range(n)] for j in range(m)]
        output_image = [[0 for i in range(n)] for j in range(m)]
        
        # building integral image concept
        for i in range(m):
            temp = 0
            for j in range(n):
                temp += mat[i][j]
                integral_image[i][j] = temp
                if i>0: integral_image[i][j] += integral_image[i-1][j]
                    
        for i in range(m):
            for j in range(n):
                r,R=max(0,i-k),min(i+k,m-1)
                c,C=max(0,j-k),min(j+k,n-1)
                output_image[i][j] = integral_image[R][C]
                if r>0: output_image[i][j] -=  integral_image[r-1][C]
                if c>0: output_image[i][j] -=  integral_image[R][c-1]
                if r>0 and c>0: output_image[i][j] +=  integral_image[r-1][c-1]
        return output_image