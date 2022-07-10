class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        l=len(shifts)
        ss=shifts[-1]
        for i in range(l-2,-1,-1):
            shifts[i]=ss+shifts[i]
            ss=shifts[i]
        res=[]
        #print(shifts)
        for i in range(l):
            c=((ord(s[i])-97)+shifts[i])%26
            c=c+97
            res.append(chr(c))
        return "".join(res)
        
        