class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        arr2=sorted(arr2,reverse=True)
        print(arr2)
        res=0
        for i in range(len(arr1)):
            n=arr1[i]
            Bool=True
            for j in range(len(arr2)):
                if abs(n-arr2[j])<=d: 
                    Bool=True
                    break
                else:
                    Bool=False
            if Bool==False: res += 1
        return res