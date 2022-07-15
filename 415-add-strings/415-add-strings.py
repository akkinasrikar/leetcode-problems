class Solution:
    def addStrings(self, num1,num2):
        d={48: 0, 49: 1, 50: 2, 51: 3, 52: 4, 53: 5, 54: 6, 55: 7, 56: 8, 57: 9}
        n1,n2=self.convert(num1,d),self.convert(num2,d)
        res=self.add(n1,n2)
        return str(res)
    def add(self,x,y):
        if y==0: return x
        else: return self.add(x^y,(x&y)<<1)
    def convert(self,num,d):
        l=len(num)-1
        t=10**l
        s,i=0,0
        while l>=0:
            s=s+d[ord(num[i])]*t
            t,i,l=t//10,i+1,l-1
        return s