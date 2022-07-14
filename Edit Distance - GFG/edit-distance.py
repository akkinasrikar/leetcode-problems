from functools import lru_cache
class Solution:
	def editDistance(self, s, t):
		# Code here
		
		@lru_cache(None)
		def dp(s,t):
		    if not s and not t: return 0
		    if not s: return len(t)
		    if not t: return len(s)
		    if s[0]==t[0]: return dp(s[1:],t[1:])
		    i=1+dp(s[1:],t)
		    d=1+dp(s,t[1:])
		    r=1+dp(s[1:],t[1:])
		    return min(i,d,r)
		    
		return dp(s,t)

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s, t = input().split()
		ob = Solution();
		ans = ob.editDistance(s, t)
		print(ans)
# } Driver Code Ends