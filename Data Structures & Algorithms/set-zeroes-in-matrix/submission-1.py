class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    for i in range(len(matrix)):
                        if matrix[i][col] != 0:
                            matrix[i][col] = "#"
                    for j in range(len(matrix[0])):
                        if matrix[row][j] != 0:
                            matrix[row][j] = "#"
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "#":
                    matrix[row][col] = 0