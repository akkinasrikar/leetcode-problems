class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        def find(l,r):
            m=(l+(r-l)//2)
            #print(l,r,m,arr[m])
            if arr[m-1]<arr[m] and arr[m]>arr[m+1]: return m
            if arr[m-1]<arr[m]: return find(m,r)
            else: return find(l,m)
                
        res=find(0,len(arr)-1)
        return res
        