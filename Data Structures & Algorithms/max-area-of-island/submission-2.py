class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        def findSize(row, col):
            if grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            size = 1
            
            if row > 0:
                size += findSize(row-1, col)
            if row < len(grid) - 1:
                size += findSize(row+1, col)
            if col > 0:
                size += findSize(row, col-1)
            if col < len(grid[0]) - 1:
                size += findSize(row, col+1)
            return size
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area = findSize(row, col)
                    if area > maxArea:
                        maxArea = area
        
        return maxArea