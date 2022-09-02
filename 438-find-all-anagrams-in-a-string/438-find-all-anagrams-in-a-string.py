class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pl,sl,res=len(p),len(s),[]
        i=0
        phash=collections.Counter(p)
        shash=collections.Counter(s[:pl])
        j=pl
        while j<=sl:
            if phash==shash: res.append(i)
            shash[s[i]] -= 1
            if shash[s[i]] <= 0: shash.pop(s[i])
            if j<sl: shash[s[j]] += 1
            i,j=i+1,j+1
        return res
                
        
        