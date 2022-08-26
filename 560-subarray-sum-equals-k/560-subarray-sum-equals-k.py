class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        SUM=0
        hashmap={0:1}
        for i in nums:
            SUM += i
            if (SUM-k) in hashmap:
                res += hashmap[SUM-k]
            if SUM not in hashmap:
                hashmap[SUM]=1
            else:
                hashmap[SUM] += 1
        return res
                
            
        