class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def N(a):
            m={}
            return [m.setdefault(c,len(m)) for c in a]
        
        x=N(pattern)
        return [w for w in words if N(w)==x]