class Solution:
    def solve(self, board: List[List[str]]) -> None:
        surrounded = []

        def bfs(startRow, startCol):
            checked = set()
            queue = deque([[startRow, startCol]])

            while queue:
                curr = queue.popleft()
                row = curr[0]
                col = curr[1]
                if row == 0 or col == 0:
                    #Touching edge: Immediately return without changing region
                    return
                if row == len(board)-1 or col == len(board[0])-1:
                    return
                #Not touching edge, so continue BFS
                checked.add((row, col))
                #Already confirmed not at edges, so don't need to check for going past borders
                if board[row-1][col] == "O" and (row-1, col) not in checked:
                    queue.append([row-1, col])
                if board[row+1][col] == "O" and (row+1, col) not in checked:
                    queue.append([row+1, col])
                if board[row][col-1] == "O" and (row, col-1) not in checked:
                    queue.append([row, col-1])
                if board[row][col+1] == "O" and (row, col+1) not in checked:
                    queue.append([row, col+1])
            #If this point is reached, queue has been exhausted
            #Entire region checked, does not touch border
            #Mark each O in region to be changed to X
            for coord in checked:
                surrounded.append(coord)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    bfs(row, col)
                    for coord in surrounded:
                        board[coord[0]][coord[1]] = "X"
                    surrounded = []