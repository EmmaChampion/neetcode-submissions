class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
     dist = [math.inf] * (n + 1)
     dist[k] = 0
     dist[0] = -1
     adj = [[] for i in range(n + 1)]
     for edge in times:
         adj[edge[0]].append([edge[2], edge[1]])

     pq = []
     heapq.heappush(pq, [0, k])
     while pq:
         curr = heapq.heappop(pq)
         for neighbor in adj[curr[1]]:
             if dist[curr[1]] + neighbor[0] < dist[neighbor[1]]:
                 dist[neighbor[1]] = dist[curr[1]] + neighbor[0]
                 heapq.heappush(pq, neighbor)

     print(dist)
     minTime = max(dist)
     if math.isinf(minTime):
         return -1
     return minTime