class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        indegree = {}
        for word in words:
            for char in word:
                if char not in adj:
                    adj[char] = []
                    indegree[char] = 0
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i+1]
            j = 0
            while j < len(w1) and j < len(w2):
                if w1[j] != w2[j]:
                    break
                j += 1
            if j == len(w1):
                continue
            if j == len(w2):
                return ""
            adj[w1[j]].append(w2[j])
            indegree[w2[j]] += 1
        
        queue = deque()
        for char, indeg in indegree.items():
            if indeg == 0:
                queue.append(char)
        result = ""

        while queue:
            curr = queue.popleft()
            print("Processing", curr)
            result += curr
            if curr not in adj:
                return ""
            for neighbor in adj[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(result) < len(adj):
            return ""
        return result