import re
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p=paragraph.lower()
        p=re.sub(r'[^\w\s]',' ',p)
        p=p.split()
        p=Counter(p)
        p=sorted(p.items(),key=lambda x:x[1],reverse=True)
        for i in p:
            if i[0] not in banned: return i[0]
        
        
              
        