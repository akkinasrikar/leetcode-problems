class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        h={}
        for i in arr:
            if i in h: return True
            h[i*2]=i
            h[i/2]=i**2
        return False
        