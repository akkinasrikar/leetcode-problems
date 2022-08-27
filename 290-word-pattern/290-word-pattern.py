class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        hp={}
        sp={}
        s=s.split(" ")
        for i in range(len(s)):
            try:
                if p[i] not in hp:
                    hp[p[i]]=s[i]
                    sp[s[i]]=p[i]
                elif hp[p[i]]==s[i] and sp[s[i]]==p[i]:
                    continue
                else: return False
            except:
                return False
        res=""
        for i in s: res += sp[i]
        #print(res)
        return res==p
                
                
        