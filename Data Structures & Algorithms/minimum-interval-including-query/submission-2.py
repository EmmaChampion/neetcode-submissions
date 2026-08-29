class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = []
        result = {}
        
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(minHeap, [intervals[i][1] - intervals[i][0] + 1, intervals[i][1]])
                i += 1
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            if minHeap:
                result[q] = minHeap[0][0]
            else:
                result[q] = -1
        
        return [result[q] for q in queries]