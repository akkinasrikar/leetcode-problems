class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        l=set(range(n))
        n=set(j for i,j in edges)
        return list(l-n)
        