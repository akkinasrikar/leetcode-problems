class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
    
        def remove(word):
            res=[]
            stack=[]
            count = 0
            for i in word:
                if i not in ["(",")"]: res.append(i)
                elif i=="(":
                    res.append("(")
                    stack.append(")")
                    count += 1
                elif i==")" and len(stack)!=0: res.append(stack.pop())
                elif i==")" and len(stack)==0: continue
            count  = count - len(stack)
            if len(stack)==0:
                return "".join(res)
            else:
                new_res=[]
                for i in res:
                    if i!="(": new_res.append(i)
                    elif i=="(" and count!=0: 
                        new_res.append(i)
                        count -= 1
                    elif i=="(" and count==0: continue
                return "".join(new_res)
        return remove(s)