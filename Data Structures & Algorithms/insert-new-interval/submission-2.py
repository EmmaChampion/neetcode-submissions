class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        if intervals[0][0] > newInterval[0]:
            loc = 0
        else:
            loc = len(intervals)
            for i in range(1, len(intervals)):
                if intervals[i][0] > newInterval[0]:
                    loc = i
                    break
        intervals.insert(loc, newInterval)
        
        while loc > 0:
            if intervals[loc - 1][1] >= intervals[loc][0]:
                intervals[loc][0] = min(intervals[loc - 1][0], intervals[loc][0])
                intervals[loc][1] = max(intervals[loc - 1][1], intervals[loc][1])
                intervals.pop(loc - 1)
                loc -= 1
            else:
                break

        while loc < len(intervals) - 1:
            if intervals[loc + 1][0] <= intervals[loc][1]:
                intervals[loc][1] = max(intervals[loc + 1][1], intervals[loc][1])
                intervals[loc][0] = min(intervals[loc + 1][0], intervals[loc][0])
                intervals.pop(loc + 1)
            else:
                break
        
        return intervals