class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        prev=values[0]+0
        final=-999999
        for i in range(1,len(values)):
            final=max(prev+values[i]-i,final)
            prev=max(values[i]+i,prev)
        return final
        