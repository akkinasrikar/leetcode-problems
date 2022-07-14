#User function Template for python3

from functools import lru_cache
#Function to find the maximum possible amount of money we can win.
class Solution:
    def optimalStrategyOfGame(self,arr, n):
        # code here
        memo={}
        def dp(l,r):
            key=(l,r)
            if key in memo: return memo[key]
            if l>r or l>=n or r<0: return 0
            a=arr[l]+min(dp(l+1,r-1),dp(l+2,r))
            b=arr[r]+min(dp(l+1,r-1),dp(l,r-2))
            memo[key]=max(a,b)
            return memo[key]
        
        return dp(0,n-1)
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        ob = Solution()
        print(ob.optimalStrategyOfGame(arr,n))

# } Driver Code Ends