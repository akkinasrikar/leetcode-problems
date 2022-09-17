class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        l=len(strs)
        
        @lru_cache(None)
        def dp(pos,m,n):
            if pos>=l: return 0
            if m==0 and n==0: return 0
            s=strs[pos]
            a,b=s.count('0'),s.count('1')
            if m-a>=0 and n-b>=0:
                return max(1+dp(pos+1,m-a,n-b),dp(pos+1,m,n))
            else:
                return dp(pos+1,m,n)
            
        return dp(0,m,n)
            
            
        