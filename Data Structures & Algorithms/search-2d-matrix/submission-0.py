class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        row_length = len(matrix[0])
        while left <= right:
            middle = (left + right) // 2
            middle_row = middle // row_length
            middle_col = middle - (middle_row * row_length)
            if target == matrix[middle_row][middle_col]:
                return True
            elif target < matrix[middle_row][middle_col]:
                right = middle - 1
            else:
                left = middle + 1
        return False