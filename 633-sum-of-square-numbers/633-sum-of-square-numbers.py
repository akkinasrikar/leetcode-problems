class Solution:
    def judgeSquareSum(self, c):
        values=[]
        for i in range(0,c+1):
            if i**2<=c:
                values.append(i**2)
            else:
                break
        values=values+values
        s=set()
        for i in range(0,len(values)):
            temp=c-values[i]
            if temp in s:
                return True
            s.add(values[i])
        
        return False
        