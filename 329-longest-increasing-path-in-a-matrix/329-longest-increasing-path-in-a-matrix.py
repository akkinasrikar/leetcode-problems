class Solution:
    def longestIncreasingPath(self, M: List[List[int]]) -> int:
        if not M or not M[0]: return 0
        m,n=len(M),len(M[0])
        @lru_cache(None)
        def dpdfs(i,j):
            val=M[i][j]
            a=dpdfs(i-1,j) if i and M[i-1][j]<val else 0
            b=dpdfs(i+1,j) if i<m-1 and M[i+1][j]<val else 0
            c=dpdfs(i,j-1) if j and M[i][j-1]<val else 0
            d=dpdfs(i,j+1) if j<n-1 and M[i][j+1]<val else 0
            return 1+max(a,b,c,d)
        res=[dpdfs(i,j) for i in range(m) for j in range(n)]
        return max(res)
        
        
                        