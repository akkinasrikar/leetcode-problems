class Solution:
    def calcEquation(self,eq,v,q):
        graph=collections.defaultdict(dict)
        for (x,y),v in zip(eq,v):
            graph[x][y]=v
            graph[y][x]=1/v
        
        def bfs(src,dst):
            if not (src in graph and dst in graph): return -1
            curr,visited=[(src,1.0)],set()
            for x,v in curr:
                if x==dst: return v
                visited.add(x)
                for y in graph[x]:
                    if y not in visited:
                        curr.append([y,v*graph[x][y]])
            return -1
        
        return [bfs(a,b) for a,b in q]
                
        