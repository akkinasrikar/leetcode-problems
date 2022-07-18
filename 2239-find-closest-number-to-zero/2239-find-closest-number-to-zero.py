class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        dst=[]
        for i in nums: dst.append([abs(i),i])
        dst=sorted(dst,key=lambda x:(x[0],-x[1]))
        return dst[0][1]