class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def findIsland(row, col):
            if grid[row][col] == "0":
                return
            grid[row][col] = "0"
            if row > 0:
                findIsland(row-1, col)
            if row < len(grid) - 1:
                findIsland(row+1, col)
            if col > 0:
                findIsland(row, col-1)
            if col < len(grid[0]) - 1:
                findIsland(row, col+1)
            

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    findIsland(row, col)
        return count