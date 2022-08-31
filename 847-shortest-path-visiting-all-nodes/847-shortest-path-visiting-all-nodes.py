class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        goal = (1 << n) - 1
        queue = collections.deque((x,1 << x) for x in range(n))
        steps = collections.defaultdict(lambda: n*n)
        for i in range(n): steps[i,1<<i]=0
        while queue:
            cn,cp=queue.popleft()
            cs=steps[cn,cp]
            if cp == goal: return cs
            for c in graph[cn]:
                chs= cp | ( 1 << c)
                if steps[c,chs]>cs+1:
                    steps[c,chs]=cs+1
                    queue.append((c,chs))