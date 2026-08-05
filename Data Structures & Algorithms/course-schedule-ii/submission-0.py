class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        #adj[n] holds the numbers of courses that n is a prereq for
        adjacency = [[] for i in range(numCourses)]
        for edge in prerequisites:
            adjacency[edge[1]].append(edge[0])
            indegree[edge[0]] += 1
        
        schedule = []
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            curr = queue.popleft()
            schedule.append(curr)
            for neighbor in adjacency[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(schedule) == numCourses:
            return schedule
        else:
            return []