class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #No cycles
        #Tree with n nodes has n-1 edges
        #Connected
        if len(edges) != n-1:
            return False

        #Check for connection
        adj = [[] for i in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        dfs(0)
        #Fully connected and correct number of edges means no cycles possible, valid tree
        if len(visited) != n:
            return False
        return True