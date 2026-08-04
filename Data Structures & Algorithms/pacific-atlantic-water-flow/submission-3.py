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
        
        def checkPacific(row, col):
            if row < len(heights) - 1 and (row+1, col) not in pacific:
                if heights[row][col] <= heights[row+1][col]:
                    pacific.add((row+1, col))
                    checkPacific(row+1, col)
            if col < len(heights[0]) - 1 and (row, col+1) not in pacific:
                if heights[row][col] <= heights[row][col+1]:
                    pacific.add((row, col+1))
                    checkPacific(row, col+1)
            if row > 0 and (row-1, col) not in pacific:
                if heights[row][col] <= heights[row-1][col]:
                    pacific.add((row-1, col))
                    checkPacific(row-1, col)
            if col > 0 and (row, col-1) not in pacific:
                if heights[row][col] <= heights[row][col-1]:
                    pacific.add((row, col-1))
                    checkPacific(row, col-1)
        
        def checkAtlantic(row, col):
            if row < len(heights) - 1 and (row+1, col) not in atlantic:
                if heights[row][col] <= heights[row+1][col]:
                    atlantic.add((row+1, col))
                    checkAtlantic(row+1, col)
            if col < len(heights[0]) - 1 and (row, col+1) not in atlantic:
                if heights[row][col] <= heights[row][col+1]:
                    atlantic.add((row, col+1))
                    checkAtlantic(row, col+1)
            if row > 0 and (row-1, col) not in atlantic:
                if heights[row][col] <= heights[row-1][col]:
                    atlantic.add((row-1, col))
                    checkAtlantic(row-1, col)
            if col > 0 and (row, col-1) not in atlantic:
                if heights[row][col] <= heights[row][col-1]:
                    atlantic.add((row, col-1))
                    checkAtlantic(row, col-1)
        
        for coord in pacific.copy():
            checkPacific(coord[0], coord[1])
        for coord in atlantic.copy():
            checkAtlantic(coord[0], coord[1])
        
        #Only count coordinates in both
        both = []
        for coord in pacific:
            if coord in atlantic:
                both.append([coord[0], coord[1]])
        return both