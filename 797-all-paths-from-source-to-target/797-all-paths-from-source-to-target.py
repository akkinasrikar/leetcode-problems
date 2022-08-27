class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)-1
        res=[]
        def dfs(temp):
            if temp[-1]==n: 
                res.append(temp)
                return
            for i in graph[temp[-1]]:
                dfs(temp+[i])
        dfs([0])
        return res
            
            