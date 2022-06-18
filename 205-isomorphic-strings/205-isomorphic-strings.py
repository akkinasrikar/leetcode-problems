class Solution:
    def isIsomorphic(self, s,t):
        d=list(zip(s,t))
        temp={}
        for i,j in d:
            if (i not in temp.keys()) and (j not in temp.values()):
                temp[i]=j
            elif (i not in temp.keys()) and (j in temp.values()):
                return False
            elif (i in temp.keys()) and (j not in temp.values()):
                return False
            elif (i in temp.keys()) and (j in temp.values()):
                if temp[i]==j:
                    continue
                else:
                    return False
        return True
            