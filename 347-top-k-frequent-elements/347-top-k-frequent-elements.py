class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s=nums
        c=Counter(s)
        c=sorted(c.items(),key=lambda x:x[1],reverse=True)
        res=[]
        for i in range(k):
            res.append(c[i][0])
        return res
            