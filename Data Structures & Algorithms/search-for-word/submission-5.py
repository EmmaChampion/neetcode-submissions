class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word = word.upper()
        if len(word) > len(board) * len(board[0]):
            return False

        def findWord(row, col, idx, checked):
            if idx < len(word) and board[row][col].upper() != word[idx]:
                return False
            if idx >= len(word) - 1:
                return True
            
            if row >= 1 and [row-1, col] not in checked:
                checked.append([row-1, col])
                if findWord(row - 1, col, idx + 1, checked):
                    return True
                checked.pop()
            if row < len(board) - 1 and [row+1, col] not in checked:
                checked.append([row+1, col])
                if findWord(row + 1, col, idx + 1, checked):
                    return True
                checked.pop()
            if col >= 1 and [row, col-1] not in checked:
                checked.append([row, col-1])
                if findWord(row, col - 1, idx + 1, checked):
                    return True
                checked.pop()
            if col < len(board[row]) - 1 and [row, col+1] not in checked:
                checked.append([row, col+1])
                if findWord(row, col + 1, idx + 1, checked):
                    return True
                checked.pop()
            return False

        for row in range(len(board)):
            for col in range(len(board[row])):
                if findWord(row, col, 0, []):
                    return True
        return False