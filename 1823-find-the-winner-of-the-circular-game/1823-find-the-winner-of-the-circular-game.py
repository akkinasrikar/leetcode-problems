class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        f=[i for i in range(1,n+1)]
        idx=0
        while len(f)>1:
            idx=(idx+k-1)%len(f)
            del f[idx]
            idx=idx%len(f)
        return f[0]
            
        
        