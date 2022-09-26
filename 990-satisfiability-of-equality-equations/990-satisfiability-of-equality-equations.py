class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        graph = collections.defaultdict(set)
        check = set()
        for i in equations:
            if i[1:3]=="!=":
                a,b=i.split("!=")
                check.add((a,b))
            else:
                a,b=i.split("==")
                graph[a].add(b)
                graph[b].add(a)
        
        def bfs(a,b):
            q = collections.deque([a])
            visited=set()
            while q:
                x=q.popleft()
                if x==b:
                    return True
                elif x not in visited:
                    visited.add(x)
                    for i in graph[x]:
                        if i not in visited:
                            q.append(i)
            return False
        
        for i,j in check:
            if bfs(i,j): return False
        return True
                        