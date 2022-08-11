class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph={i:[] for i in range(n)}
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        #print(graph)
        visited=set()
        def bfs(src,dst):
            if src==dst: return True
            q=graph[src]
            visited.add(src)
            for i in q:
                if i not in visited:
                    if bfs(i,dst):
                        return True
            return False
        
        return bfs(source,destination)
                    
        