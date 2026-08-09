class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #[weight, srcIdx, destIdx] for each edge
        edges = []
        for src in range(len(points)):
            for dest in range(src + 1, len(points)):
                dist = abs(points[src][0] - points[dest][0]) + abs(points[src][1] - points[dest][1])
                edges.append([dist, src, dest])
        edges.sort(reverse=True)
        
        parent = [i for i in range(len(points))]
        rank = [0] * len(points)

        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        numEdges = 0
        cost = 0
        while numEdges < len(points) - 1:
            edge = edges.pop()
            if union(edge[1], edge[2]):
                numEdges += 1
                cost += edge[0]
        
        return cost