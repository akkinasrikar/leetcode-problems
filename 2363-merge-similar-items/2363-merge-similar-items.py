class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        hmp={}
        for i in items1:
            hmp[i[0]] = hmp.get(i[0],0)+i[1]
        for i in items2:
            hmp[i[0]] = hmp.get(i[0],0)+i[1]
        res=[[i,hmp[i]] for i in hmp]
        res=sorted(res,key=lambda x:x[0],reverse=False)
        return res
        