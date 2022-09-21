class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        res,cnt=[],Counter(changed)
        if len(changed)%2: return []
        for i in sorted(cnt.keys()):
            if cnt[i]>cnt[i*2]: return []
            if i==0:
                if cnt[i]%2: return []
                else: res += [0]*(cnt[i]//2)
            else:
                res += [i]*cnt[i]
            cnt[i*2] -= cnt[i]
        return res
                
        