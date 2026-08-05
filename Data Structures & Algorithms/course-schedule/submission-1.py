class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency = {}
        for edge in prerequisites:
            if edge[0] in adjacency:
                adjacency[edge[0]].append(edge[1])
            else:
                adjacency[edge[0]] = [edge[1]]
        #0 = unvisited, 1 = in recursion stack, 2 = cleared
        color = [0] * numCourses

        #Immediately return false when a cycle is detected
        def dfs(node):
            if node in adjacency:
                neighbors = adjacency[node]
            else:
                color[node] = 2
                return True

            color[node] = 1
            possible = True
            for neighbor in neighbors:
                if color[neighbor] == 1:
                    return False
                if color[neighbor] == 2:
                    continue
                if not dfs(neighbor):
                    possible = False
            color[node] = 2
            return possible
        
        for course in range(numCourses):
            if color[course] == 2:
                continue
            if not dfs(course):
                return False
        return True