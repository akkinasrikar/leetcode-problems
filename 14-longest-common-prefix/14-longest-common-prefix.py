class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs)==1 or len(set(strs))==1:
            return strs[0]
        l=len(strs)
        s,temp=1,[]
        while True:
            nw=[i[0:s] for i in strs]
            if len(set(nw))==1:
                s += 1
                temp=nw
                continue
            else:
                break
        if temp==[]: return ""
        return temp[0]