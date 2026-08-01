class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        defaultBoard = ["." * n] * n
        rows = [False] * n
        
        def backtrack(col, board, rowTaken):
            if col >= n:
                result.append(board.copy())
                return
            for row in range(len(board)):
                if rowTaken[row]:
                    continue
                if self.checkUpLeft(board, row, col) and self.checkDownLeft(board, row, col, n):
                    temp = board[row]
                    board[row] = board[row][:col] + "Q" + board[row][col+1:]
                    rowTaken[row] = True
                    backtrack(col + 1, board, rowTaken)
                    board[row] = temp
                    rowTaken[row] = False
        
        backtrack(0, defaultBoard, rows)
        return result
    
    #Returns true if no queens in upper left diagonal from row,col
    def checkUpLeft(self, board, row, col):
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1
        return True
    
    #Returns true if no queens in lower left diagonal from row,col
    def checkDownLeft(self, board, row, col, n):
        while col >= 0 and row < n:
            if board[row][col] == "Q":
                return False
            col -= 1
            row += 1
        return True