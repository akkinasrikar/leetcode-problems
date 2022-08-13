class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        hashmap={i:0 for i in range(1,n+1)}
        for a,b in trust:
            hashmap[a] -= 1
            hashmap[b] += 1
        for i in range(1,n+1):
            if hashmap[i]==n-1: return i
        return -1