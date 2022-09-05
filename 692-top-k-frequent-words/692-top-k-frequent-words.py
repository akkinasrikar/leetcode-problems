class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d={}
        for i in words: d[i]=d.get(i,0)+1
        res=sorted(d,key=lambda x:(-d[x],x))
        return res[:k]