class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i,j=0,0
        Max=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j] and i<=j:
                Max=max(Max,j-i)
                j += 1
            elif nums1[i]>nums2[j] and i<=j:
                i += 1
                j += 1
        return Max
            
            
        