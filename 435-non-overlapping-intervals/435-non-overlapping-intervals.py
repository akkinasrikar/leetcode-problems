class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ints=sorted(intervals,key=lambda x:x[0])
        prev=ints[0][1]
        res=0
        for start,end in ints[1:]:
            if start>=prev: prev=end
            else: res,prev=res+1,min(end,prev)
        return res