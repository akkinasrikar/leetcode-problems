class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        T=triangle
        @lru_cache(None)
        def dp(i,j):
            if i==len(T): return 0
            return T[i][j]+min(dp(i+1,j),dp(i+1,j+1))
        return dp(0,0)