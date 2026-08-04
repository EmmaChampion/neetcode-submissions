class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic= set()
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if row == 0 or col == 0:
                    pacific.add((row, col))
                if row == len(heights) - 1 or col == len(heights[0]) - 1:
                    atlantic.add((row,col))
        
        def dfs(row, col, ocean):
            if row < len(heights) - 1 and (row+1, col) not in ocean:
                if heights[row][col] <= heights[row+1][col]:
                    ocean.add((row+1, col))
                    dfs(row+1, col, ocean)
            if col < len(heights[0]) - 1 and (row, col+1) not in ocean:
                if heights[row][col] <= heights[row][col+1]:
                    ocean.add((row, col+1))
                    dfs(row, col+1, ocean)
            if row > 0 and (row-1, col) not in ocean:
                if heights[row][col] <= heights[row-1][col]:
                    ocean.add((row-1, col))
                    dfs(row-1, col, ocean)
            if col > 0 and (row, col-1) not in ocean:
                if heights[row][col] <= heights[row][col-1]:
                    ocean.add((row, col-1))
                    dfs(row, col-1, ocean)
        
        for coord in pacific.copy():
            dfs(coord[0], coord[1], pacific)
        for coord in atlantic.copy():
            dfs(coord[0], coord[1], atlantic)
        
        #Only count coordinates in both
        both = []
        for coord in pacific:
            if coord in atlantic:
                both.append([coord[0], coord[1]])
        return both