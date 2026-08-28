"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) <= 1:
            return len(intervals)
        intervals.sort(key=lambda interval: interval.start)
        roomEnds = []
        heapq.heappush(roomEnds, intervals[0].end)
        for i in range(1, len(intervals)):
            if intervals[i].start >= roomEnds[0]:
                heapq.heappop(roomEnds)
            heapq.heappush(roomEnds, intervals[i].end)
        return len(roomEnds)
            