from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=dict(Counter(nums1))
        b=dict(Counter(nums2))
        res=[]
        for i in a.keys():
            if i in b.keys():
                for j in range(min(a[i],b[i])): res.append(i)
        return res
        
