from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        numsfreq=[]
        for i in c:
            numsfreq.append([i,c[i]])
        #print(numsfreq)
        nums=sorted(numsfreq,key=lambda x:(x[1],-x[0]))
        res=[]
        for i in nums:
            res += [i[0]]*i[1]
        return res