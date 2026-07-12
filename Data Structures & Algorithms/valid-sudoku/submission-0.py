class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        found = [False] * 9
        #Check rows
        for row in board:
            for val in row:
                if val.isdigit():
                    val = int(val)
                    if found[val - 1]:
                        return False
                    else:
                        found[val - 1] = True
            found = [False] * 9
        
        #Check columns
        for col in range(9):
            for row in range(9):
                val = board[row][col]
                if val.isdigit():
                    val = int(val)
                    if found[val - 1]:
                        return False
                    else:
                        found[val - 1] = True
            found = [False] * 9
        
        #Make a new array with rows coming from blocks
        blocks = [[] for i in range(9)]
        #First row of blocks
        for row in range(3):
            for col in range(9):
                if col < 3:
                    blocks[0].append(board[row][col])
                elif col > 5:
                    blocks[2].append(board[row][col])
                else:
                    blocks[1].append(board[row][col])
        
        #Second row of blocks
        for row in range(3, 6):
            for col in range(9):
                if col < 3:
                    blocks[3].append(board[row][col])
                elif col > 5:
                    blocks[5].append(board[row][col])
                else:
                    blocks[4].append(board[row][col])
        
        #Third row of blocks
        for row in range(6,9):
            for col in range(9):
                if col < 3:
                    blocks[6].append(board[row][col])
                elif col > 5:
                    blocks[8].append(board[row][col])
                else:
                    blocks[7].append(board[row][col])
        
        #Check blocks
        for row in blocks:
            for val in row:
                if val.isdigit():
                    val = int(val)
                    if found[val - 1]:
                        return False
                    else:
                        found[val - 1] = True
            found = [False] * 9

        return True












