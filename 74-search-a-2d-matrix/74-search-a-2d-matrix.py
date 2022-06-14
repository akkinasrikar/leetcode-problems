class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:   
        
        def search(i,target,l,r):
            if l<=r:
                m=l+(r-l)//2
                if target==i[m]: return True
                if target<i[m]: return search(i,target,l,m-1)
                else: return search(i,target,m+1,r)
            else: 
                return False
        for i in matrix:
            if i[-1]==target: return True
            if target<i[-1]:
                return search(i,target,0,len(i)-1)