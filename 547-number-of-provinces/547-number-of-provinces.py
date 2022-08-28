class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res=[]
        v=isConnected
        if not v: return 0
        visited=set()
        def dfs(node):
            for i,j in enumerate(v[node]):
                if i not in visited and j==1:
                    visited.add(i)
                    dfs(i)
        c=0
        for i in range(len(v)):
            if i not in visited:
                dfs(i)
                c += 1
        return c
            
                    
        