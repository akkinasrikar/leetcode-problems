class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        i,j=m-1,0
        count = 0
        while (i>=0 and j>=0 and i<m and j<n):
            if grid[i][j]<0:
                count += n-j
                i -= 1
            else:
                j += 1
        return count
        