class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res=[[sum(val),i] for i,val in enumerate(mat)]
        res=sorted(res,key=lambda x:(x[0],x[1]))
        return [res[i][1] for i in range(k)]