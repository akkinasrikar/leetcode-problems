class Solution:
    def merge(self, intervals):
        intervals=sorted(intervals,key=lambda x:x[0])
        top=intervals[0]
        res=[]
        for pair in intervals:
            if pair[0]<=top[1]:
                top[1]=max(top[1],pair[1])
            else:
                res.append(top)
                top=pair
        res.append(top)
        return res