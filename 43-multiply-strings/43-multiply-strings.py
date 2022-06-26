class Solution:
    def multiply(self, num1, num2):
        return str(self.number(num1)*self.number(num2))
    def number(self,n):
        d={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        l=len(n)-1
        st=10**l
        val=0
        for i in n:
            val=val+d[i]*st
            st=st//10
        return int(val)