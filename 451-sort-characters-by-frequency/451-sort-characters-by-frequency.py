from collections import Counter
class Solution:
    def frequencySort(self, s):
        c=Counter(s)
        c=sorted(c.items(),key=lambda x:x[1],reverse=True)
        s=""
        for i in c:
            s=s+i[0]*i[1]
        return s
        