class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        res=[]
        def bfs(l,d,s,p):
            if l==n:
                res.append(int(s))
                return
            if l==0:
                for i in range(1,10):
                    bfs(l+1,d,s+str(i),i)
            else:
                if (d+p)<=9:
                    bfs(l+1,d,s+str(d+p),d+p)
                if (p-d)>=0:
                    bfs(l+1,d,s+str(p-d),p-d)             
        
        bfs(0,k,"",0)
        return list(set(res))
                
        