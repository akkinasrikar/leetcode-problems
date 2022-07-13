#User function Template for python3
from functools import lru_cache
class Solution:
	def minDifference(self, arr, n):
		# code here
		@lru_cache(None)
		def dp(idx,sum1,sum2):
		    if idx==n: return abs(sum1-sum2)
		    include=dp(idx+1,arr[idx]+sum1,sum2)
		    exclude=dp(idx+1,sum1,arr[idx]+sum2)
		    return min(include,exclude)
		return dp(0,0,0)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends