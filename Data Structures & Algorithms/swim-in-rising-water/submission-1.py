class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        maxHeight = 0
        pq = []
        heapq.heappush(pq, [grid[0][0], [0,0]])
        visited = set()

        while pq:
            curr = heapq.heappop(pq)
            if curr[0] > maxHeight:
                maxHeight = curr[0]
            row = curr[1][0]
            col = curr[1][1]
            visited.add((row, col))
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return maxHeight
            if row < len(grid) - 1 and (row+1, col) not in visited:
                heapq.heappush(pq, [grid[row+1][col],[row+1, col]])
            if col < len(grid[0])-1 and (row,col+1) not in visited:
                heapq.heappush(pq, [grid[row][col+1],[row, col+1]])
            if row > 0 and (row-1, col) not in visited:
                heapq.heappush(pq, [grid[row-1][col], [row-1,col]])
            if col > 0 and (row, col-1) not in visited:
                heapq.heappush(pq, [grid[row][col-1], [row,col-1]])