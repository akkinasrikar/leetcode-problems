class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        cache=[arr[0]]
        for i in range(1,len(arr)):
            cache.append(arr[i]^cache[-1])
        res=[]
        for i in queries:
            a,b=i
            if a==0: res.append(cache[b])
            else: res.append(cache[b]^cache[a-1])
        return res
        