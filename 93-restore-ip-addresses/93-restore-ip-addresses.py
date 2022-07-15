class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res=[]
        if len(s)>12: return res
        def dfs(i,dots,curip):
            if dots==4 and i==len(s):
                res.append(curip[:-1])
                return
            if dots>4: return
            for j in range(i,min(i+3,len(s))):
                t=s[i:j+1]
                if int(t)<=255 and (len(t)==1 or s[i]!='0'):
                    dfs(j+1,dots+1,curip+t+".")
        
        dfs(0,0,"")
        return res