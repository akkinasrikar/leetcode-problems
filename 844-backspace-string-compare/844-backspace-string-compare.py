class Solution(object):
    def backspaceCompare(self, s,t):
        return self.check(s)==self.check(t)
    def check(self,string):
        ls=[]
        for i in string:
            if i=="#":
                try:
                    ls.pop()
                except:
                    pass
            else:
                ls.append(i)
        return "".join(ls)
        