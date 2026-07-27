class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #Contains [distance, index] for each point
        distances = []
        for i in range(len(points)):
            distance = math.sqrt((points[i][0])**2 + (points[i][1])**2)
            distances.append([distance, i])
        heapq.heapify(distances)

        result = []
        while len(result) < k:
            point = heapq.heappop(distances)
            result.append([ (points[point[1]][0]), (points[point[1]][1]) ])
        
        return result