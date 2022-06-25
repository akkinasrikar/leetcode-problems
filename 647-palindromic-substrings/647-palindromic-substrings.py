class Solution:
    def countSubstrings(self, s: str) -> int:
        
        L=len(s)
        def getpalindromes(l,r):
            pals = []
            count = 0
            while l>=0 and r<L and s[l]==s[r]:
                pals.append(s[l:r+1])
                l -= 1
                r += 1
                count += 1
            return pals,count
        finalcount = 0
        res = []
        for i in range(L):
            a,b = getpalindromes(i,i)
            c,d = getpalindromes(i,i+1)
            res += a
            res += c
            finalcount += b
            finalcount += d
        
        #print(res)
        return finalcount
            