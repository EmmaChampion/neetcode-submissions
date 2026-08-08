class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        for src, dest in tickets:
            if src in adj:
                adj[src].append(dest)
            else:
                adj[src] = [dest]       
        for src in adj.keys():
            list.sort(adj[src], reverse=True)
        
        result = []
        def dfs(src):
            if src not in adj:
                result.append(src)
                return
            while len(adj[src]) > 0:
                next = adj[src].pop()
                dfs(next)
            result.append(src)
        
        dfs("JFK")
        result.reverse()
        return result