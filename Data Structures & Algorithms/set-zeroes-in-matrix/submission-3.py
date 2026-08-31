class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowZero = False
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    if row > 0:
                        matrix[row][0] = 0
                    else:
                        rowZero = True
        
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
                
        if matrix[0][0] == 0:
            for row in range(1, len(matrix)):
                matrix[row][0] = 0
        if rowZero:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0