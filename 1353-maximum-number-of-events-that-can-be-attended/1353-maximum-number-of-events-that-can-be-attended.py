class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n=len(events)
        events=sorted(events,key=lambda x:x[0])
        started=[]
        count,i=0,0
        curr_date=events[0][0]
        while i<n:
            while i<n and events[i][0]==curr_date:
                heappush(started,events[i][1])
                i += 1
            heappop(started)
            count += 1
            curr_date += 1
            while started and started[0]<curr_date:
                heappop(started)
            if i<n and not started: curr_date=events[i][0]
        while started:
            if heappop(started)>=curr_date:
                curr_date += 1
                count += 1
        return count
            
# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/discuss/1564595/Python-Faster-than-90-Low-space-Simple-Min-Heap-Explained   