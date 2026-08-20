class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [[-1] * len(word2) for i in range(len(word1))]
        
        def backtrack(i, j):
            if i >= len(word1):
                return len(word2) - j
            if j >= len(word2):
                return len(word1) - i
            
            if memo[i][j] != -1:
                return memo[i][j]

            if word1[i] == word2[j]:
                memo[i][j] = backtrack(i+1, j+1)
            else:
                '''# Replace
                backtrack(i+1, j+1, changes+1)
                # Add
                backtrack(i, j+1, changes+1)
                # Remove
                backtrack(i+1, j, changes+1)'''
                memo[i][j] = 1 + min(backtrack(i+1, j+1), backtrack(i, j+1), backtrack(i+1, j))
            return memo[i][j]
        
        return backtrack(0, 0)
            