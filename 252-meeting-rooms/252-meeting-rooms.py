class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals: return True
        intervals.sort()
        start=intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i][0]>=start[1]:
                start=intervals[i]
            else: return False
        return True
                
        