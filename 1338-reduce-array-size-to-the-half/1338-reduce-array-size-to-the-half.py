from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c=Counter(arr)
        c=sorted(c.items(),key=lambda x:x[1],reverse=True)
        l=len(arr)
        hl=l//2
        s=0
        count=0
        for i in c:
            s=s+i[1]
            count += 1
            if s>=hl:
                return count