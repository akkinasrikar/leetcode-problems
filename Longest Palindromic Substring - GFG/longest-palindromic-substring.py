#User function Template for python3

class Solution:
    def longestPalindrome(self, S):
        # code here
        L=len(S)
        def ispal(l,r):
            while l>=0 and r<L and S[l]==S[r]:
                l -= 1
                r += 1
            return S[l+1:r]
        
        res=""
        for i in range(L):
            res=max(res,ispal(i,i),ispal(i,i+1),key=len)
        return res
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        S = input().strip()
        ob=Solution()
        print(ob.longestPalindrome(S))
# } Driver Code Ends