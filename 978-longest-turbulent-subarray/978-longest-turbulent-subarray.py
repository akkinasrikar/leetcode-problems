class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res=0
        m=0
        for i in range(len(arr)):
            if i>=2 and (arr[i-2]>arr[i-1]<arr[i] or arr[i-2]<arr[i-1]>arr[i]):
                res += 1
            elif i>=1 and arr[i-1]!=arr[i]:
                res =2
            else:
                res=1
            m=max(m,res)
        return m
        
        