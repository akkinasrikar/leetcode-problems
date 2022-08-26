class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l,s,p,res=len(arr),1,0,0
        while k:
            if p<l:
                if s==arr[p]: s,p = s+1,p+1
                else: res,k,s = s,k-1,s+1
            else:  res,k,s = s,k-1,s+1
        return res
        
            
        