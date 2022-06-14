class Solution:
    def isValid(self, s: str) -> bool:
        l="([{"
        r=")]}"
        stack = []
        for i in s:
            if i in l:
                stack.append(r[l.index(i)])
            else:
                if len(stack)!=0:
                    temp=stack.pop()
                    if temp==i:
                        continue
                    else:
                        return False
                else: return False
        if len(stack)!=0: return False
        return True
                
        
        