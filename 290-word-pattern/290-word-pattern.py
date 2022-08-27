class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        s=s.split(" ")
        return [p.index(i) for i in p]==[s.index(i) for i in s]
                
        