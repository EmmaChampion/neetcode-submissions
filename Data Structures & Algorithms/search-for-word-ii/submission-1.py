class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = self.buildTrie(words)
        result = set()
        visited = []
        for row in range(len(board)):
            visited.append([False] * len(board[0]))

        def backtrack(row, col, trie, visited):
            if visited[row][col]:
                return
            if board[row][col] not in trie:
                return
            trie = trie[board[row][col]]
            visited[row][col] = True
            if row > 0:
                backtrack(row-1, col, trie, visited)
            if row < len(board) - 1:
                backtrack(row+1, col, trie, visited)
            if col > 0:
                backtrack(row, col-1, trie, visited)
            if col < len(board[0]) - 1:
                backtrack(row, col+1, trie, visited)
            if "End" in trie:
                idx = trie["End"]
                result.add(words[idx])
            visited[row][col] = False
            
        
        for row in range(len(board)):
            for col in range(len(board[row])):
                backtrack(row, col, trie, visited)
        return list(result)


    def buildTrie(self, words):
        root = {}
        for i in range(len(words)):
            trie = root
            for char in words[i]:
                if char not in trie:
                    trie[char] = {}
                trie = trie[char]
            trie["End"] = i
        return root