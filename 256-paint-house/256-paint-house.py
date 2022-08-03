class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        l=len(costs)
        idxs={0:[1,2],1:[0,2],2:[0,1]}
        def dp(a,b,c):
            t=str(a)+str(b)
            if a>=l: return 0
            if t in c: return c[t]
            x,y=idxs[b]
            c[t] = min(costs[a][b]+dp(a+1,x,c),
                       costs[a][b]+dp(a+1,y,c))
            return c[t]
        m,n,v={},{},{}
        q,w,e=dp(0,0,m),dp(0,1,n),dp(0,2,v)
        return min(q,w,e)
            
        