#User function Template for python3
from functools import lru_cache
class Solution:
	def longestIncreasingPath(self, M):
		#Code here
        m,n=len(M),len(M[0])
        @lru_cache(None)
        def dp(i,j):
            val=M[i][j]
            res=0
            directions=[[i+1,j],[i-1,j],[i,j+1],[i,j-1]]
            for i in directions:
                a,b=i
                if 0<=a<m and 0<=b<n and M[a][b]<val:
                    res=max(res,dp(a,b))
            return 1+res
        
        res=[dp(x,y) for x in range(m) for y in range(n)]
        return max(res)
                
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int, input().split())))
		obj = Solution()
		ans = obj.longestIncreasingPath(matrix)
		print(ans)

# } Driver Code Ends