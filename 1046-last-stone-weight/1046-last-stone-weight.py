import heapq as hp
class Solution:
    def lastStoneWeight(self, s: List[int]) -> int:
        s=[-x for x in s]
        hp.heapify(s)
        while len(s)>1 and s[0]!=0:
            hp.heappush(s,hp.heappop(s)-hp.heappop(s))
        return -s[0]