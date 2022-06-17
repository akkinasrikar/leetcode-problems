class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        
        obg = obstacleGrid 
        if obg[0][0]==1 or obg[-1][-1]==1: return 0
        m,n=len(obg),len(obg[0])
        
        @lru_cache(None)
        def dp(m,n):
            if m==1 and n==1: return 1
            if m==0 or n==0: return 0
            if obg[m-1][n-1]==1: return 0
            return dp(m-1,n)+dp(m,n-1)
    
        return dp(m,n)
        
        