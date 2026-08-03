class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        visited = []
        for row in grid:
            visited.append([False] * len(grid[0]))
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    queue.append([row, col])
                    visited[row][col] = True
        
        dist = 0
        while queue:
            qLen = len(queue)
            for i in range(qLen):
                curr = queue.popleft()
                row = curr[0]
                col = curr[1]
                grid[row][col] = dist

                #Up
                if row > 0 and not visited[row-1][col]:
                    if grid[row-1][col] != -1:
                        visited[row-1][col] = True
                        queue.append([row-1, col])
                #Down
                if row < len(grid) - 1 and not visited[row+1][col]:
                    if grid[row+1][col] != -1:
                        visited[row+1][col] = True
                        queue.append([row+1, col])
                #Left
                if col > 0 and not visited[row][col-1]:
                    if grid[row][col-1] != -1:
                        visited[row][col-1] = True
                        queue.append([row, col-1])
                #Right
                if col< len(grid[0])-1 and not visited[row][col+1]:
                    if grid[row][col+1] != -1:
                        visited[row][col+1] = True
                        queue.append([row, col+1])
            dist += 1