#User function Template for python3
from functools import lru_cache
class Solution:
    def cutRod(self, price, n):
        #code here
        @lru_cache(None)
        def dp(idx,n):
            if n<=0 or idx>n: return 0
            a=price[idx-1]+dp(idx,n-idx)
            b=dp(idx+1,n)
            return max(a,b)
            
        
        return dp(1,n)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends