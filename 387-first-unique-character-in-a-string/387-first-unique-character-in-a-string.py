class Solution:
    def firstUniqChar(self, s: str) -> int:
        c=Counter(s)
        c=sorted(c.items(),key=lambda x:x[1])
        nw=[]
        for i in c:
            if i[1]==1: nw.append(s.index(i[0]))
            else: break
        if len(nw)==0:
            return -1
        return min(nw)
        
                