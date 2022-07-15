class Solution:
    def partition(self, s: str):
        res=[]
        
        def dfs(s,path):
            if not s: 
                res.append(path)
                return 
            for i in range(1,len(s)+1):
                if ispal(s[:i]):
                    dfs(s[i:],path+[s[:i]])
        def ispal(w):
            l=len(w)
            if l%2==0:
                a,b=l//2-1,l//2
            else:
                a,b=l//2,l//2
            while a>=0 and b<l:
                if w[a]==w[b]:
                    a -= 1
                    b += 1
                else: return False
            return True
        dfs(s,[])
        return res
                    
        