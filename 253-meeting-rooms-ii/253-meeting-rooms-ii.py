import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals=sorted(intervals,key=lambda x:x[0])
        heap=[]
        for i in intervals:
            if heap and heap[0]<=i[0]:
                heapq.heapreplace(heap,i[-1])
            else:
                heapq.heappush(heap,i[-1])
        return len(heap)        
        
            