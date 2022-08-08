class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs=sorted(pairs,key=lambda x:(x[0],x[1]))
        
        @lru_cache(None)
        def dp(pos,b):
            if pos>=len(pairs): return 0
            c=pairs[pos][0]
            if b<c: return 1+dp(pos+1,pairs[pos][1])
            else: return max(dp(pos+1,b),dp(pos+1,pairs[pos][1]))
        
        return 1+dp(1,pairs[0][1])
        