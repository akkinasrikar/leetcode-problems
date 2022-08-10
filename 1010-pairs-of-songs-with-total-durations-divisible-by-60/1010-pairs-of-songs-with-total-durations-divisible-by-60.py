class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hashmap={}
        pairs=0
        for i in time:
            rem=i%60
            if rem==0:
                if 0 in hashmap: pairs += hashmap[0]
            elif 60-rem in hashmap:
                pairs += hashmap[60-rem]
            if rem in hashmap: hashmap[rem] += 1
            else: hashmap[rem]=1
        return pairs
        