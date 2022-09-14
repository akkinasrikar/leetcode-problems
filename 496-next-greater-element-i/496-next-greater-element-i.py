class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        l=len(nums2)
        for i in nums1:
            f=0
            idx=nums2.index(i)
            if idx==l-1: res.append(-1)
            else:
                for j in range(idx+1,l):
                    if nums2[j]>nums2[idx]: 
                        res.append(nums2[j])
                        f=1
                        break
                if f==0:
                    res.append(-1)
        return res
                    
        