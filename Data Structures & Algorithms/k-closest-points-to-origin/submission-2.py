class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            distance = math.sqrt(points[i][0] ** 2 + points[i][1] ** 2)
            points[i] = [distance, points[i][0], points[i][1]]
        heapq.heapify(points)

        result = []
        while len(result) < k:
            curr = heapq.heappop(points)
            result.append([curr[1], curr[2]])
        
        return result