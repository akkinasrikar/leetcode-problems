class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        hashmap={0:1}
        prefixsum=0
        for i in nums:
            prefixsum += i
            diff = prefixsum - k
            if diff in hashmap: res += hashmap[diff]
            if prefixsum not in hashmap: hashmap[prefixsum] = 1
            else: hashmap[prefixsum] += 1
        return res
        