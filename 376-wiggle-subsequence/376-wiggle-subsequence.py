class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        nan=float("nan")
        diff=[a-b for a,b in zip([nan]+nums,nums+[nan]) if a-b]
        #print(diff)
        res=[not c*d>=0 for c,d in zip(diff,diff[1:])]
        #print(res)
        return sum(res)