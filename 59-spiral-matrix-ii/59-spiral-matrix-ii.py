class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top = 0
        left = 0
        bottom = n-1
        right = n-1
        
        matrix = [[0]*n for j in range(n)]
        direction = 1
        value=1
        while top<=bottom and left <=right:
            if direction==1: # move left to right
                for i in range(left,right+1):
                    matrix[top][i]=value
                    value += 1
                top += 1
                direction = 2
            elif direction==2: # move top to bottom
                for i in range(top,bottom+1):
                    matrix[i][right]=value
                    value += 1
                right -= 1
                direction = 3
            elif direction==3: # move right to left
                for i in range(right,left-1,-1):
                    matrix[bottom][i]=value
                    value += 1
                bottom -= 1
                direction = 4
            else: # move bottom to top 
                for i in range(bottom,top-1,-1): 
                    matrix[i][left]=value
                    value += 1
                left += 1
                direction = 1
        return matrix
                    