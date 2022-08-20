class Solution:
    def simplifyPath(self, path: str) -> str:
        qs=path.split("/")
        stack=[]
        for i in qs:
            if i!='' and i!='.' and i!="..": stack.append(i)
            elif stack and i=="..": stack.pop()
        if not stack: return "/"
        res="/"
        for i in stack:
            res=res+i+"/"
        return res[:-1]
            
        
        