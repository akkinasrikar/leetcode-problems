class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(1,len(arr)-1):
            if abs(arr[i]-arr[i-1])==abs(arr[i]-arr[i+1]):
                continue
            else: return False
        return True
            
        