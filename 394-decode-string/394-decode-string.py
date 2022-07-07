class Solution:
    def decodeString(self, s):
        if "[" in s:
            st,ed=0,0
            for i in range(len(s)):
                if s[i]=="[":
                    st=i
                elif s[i]=="]":
                    ed=i
                    break
            n=""
            ne=st-1
            while True:
                if 48<=ord(s[ne])<=57:
                    n=s[ne]+n
                    ne=ne-1
                else:
                    break
            o_s=n+s[st:ed+1]
            nw=s[st+1:ed]*int(n)
            s=s.replace(o_s,nw)
            return self.decodeString(s)
        else:
            return s
            
            