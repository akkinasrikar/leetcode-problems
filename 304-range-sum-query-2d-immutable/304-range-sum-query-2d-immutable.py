# integral image concept

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        mat=matrix
        m,n=len(mat),len(mat[0])
        integral_image = [[0 for i in range(n)] for i in range(m)]
        for i in range(m):
            temp = 0
            for j in range(n):
                temp += mat[i][j]
                integral_image[i][j] = temp
                if i>0: integral_image[i][j] += integral_image[i-1][j]
        self.ig=integral_image
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res=self.ig[row2][col2]
        if row1>0: res -= self.ig[row1-1][col2]
        if col1>0: res -= self.ig[row2][col1-1]
        if row1>0 and col1>0: res += self.ig[row1-1][col1-1]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)