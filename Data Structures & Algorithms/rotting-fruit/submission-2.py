class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #Find all already rotten fruit
        queue = deque()
        visited = []
        for row in grid:
            visited.append([False] * len(grid[0]))
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append([row,col])
                    visited[row][col] = True
        #Check if there are no fruit at all
        if not queue:
            for row in grid:
                for cell in row:
                    if cell == 1:
                        #There is at least one fresh fruit, no rotten
                        return -1
            #No fruit at all
            return 0
        
        time = -1
        #While rotten fruit have neightbors, rot them and increment time
        while queue:
            qLen = len(queue)
            for i in range(qLen):
                curr = queue.popleft()
                row = curr[0]
                col = curr[1]

                #Up
                if row > 0 and not visited[row-1][col]:
                    if grid[row-1][col] == 1:
                        grid[row-1][col] = 2
                        visited[row-1][col] = True
                        queue.append([row-1, col])
                #Down
                if row < len(grid)-1 and not visited[row+1][col]:
                    if grid[row+1][col] == 1:
                        grid[row+1][col] = 2
                        visited[row+1][col] = True
                        queue.append([row+1, col])
                #Left
                if col > 0 and not visited[row][col-1]:
                    if grid[row][col-1] == 1:
                        grid[row][col-1] = 2
                        visited[row][col-1] = True
                        queue.append([row, col-1])
                #Right
                if col< len(grid[0])-1 and not visited[row][col+1]:
                    if grid[row][col+1]:
                        grid[row][col+1] = 2
                        visited[row][col+1] = True
                        queue.append([row, col+1])
            time += 1
        
        #Check if any fresh fruit are left
        for row in grid:
            for fruit in row:
                if fruit == 1:
                    return -1
        return time