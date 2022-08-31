class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        l=len(arr)
        
        def bfs(p):
            if not 0<=p<l or arr[p]<0: return False
            if arr[p]==0: return True
            arr[p] = -arr[p]
            return bfs(p+arr[p]) or bfs(p-arr[p])
        
        return bfs(start)
        