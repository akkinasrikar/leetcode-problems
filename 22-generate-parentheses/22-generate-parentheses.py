class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(l,r,path):
            if l>r or l<0 or r<0: return
            if l==0 and r==0: res.append(path)
            dfs(l-1,r,path+"(")
            dfs(l,r-1,path+")")
        dfs(n,n,"")
        return res