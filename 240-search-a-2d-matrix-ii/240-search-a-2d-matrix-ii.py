class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        m,n=len(matrix),len(matrix[0])
        x,y=0,m-1
        while True:
            if x>=n or y<0: break
            current = matrix[y][x]
            if current==target: return True
            elif target>current: x += 1
            else: y -= 1
        return False