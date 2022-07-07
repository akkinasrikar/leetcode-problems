class Solution:
    def calculate(self, s: str) -> int:
        n,stack,op=0,[],"+"
        for c,i in enumerate(s):
            if i.isnumeric():
                n=n*10+int(i)
            if i in "+-*/" or c==len(s)-1:
                if op=="+": stack.append(n)
                elif op=="-": stack.append(-n)
                elif op=="*": stack.append(n*stack.pop())
                elif op=="/": stack.append(int(stack.pop()/n))
                n,op=0,i
                
        return sum(stack)
                    
                
        