class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hmap={}
        srt=s[:10]
        hmap[srt]=1
        for i in range(10,len(s)):
            srt=srt[1:]+s[i]
            if srt in hmap: hmap[srt]+=1
            else: hmap[srt]=1
        res=[]
        for i in hmap:
            if hmap[i]>=2: res.append(i)
        return res