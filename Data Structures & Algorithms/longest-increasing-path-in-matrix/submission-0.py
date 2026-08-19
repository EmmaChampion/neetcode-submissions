class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = [[-1] * len(matrix[0]) for i in range(len(matrix))]

        def dfs(i, j):
            if memo[i][j] != -1:
                return memo[i][j]
            longest = 1
            if i > 0 and matrix[i-1][j] > matrix[i][j]:
                longest = max(longest, 1 + dfs(i-1, j))
            if i < len(matrix)-1 and matrix[i+1][j] > matrix[i][j]:
                longest = max(longest, 1 + dfs(i+1, j))
            if j > 0 and matrix[i][j-1] > matrix[i][j]:
                longest = max(longest, 1 + dfs(i, j-1))
            if j<len(matrix[0])-1 and matrix[i][j+1] >matrix[i][j]:
                longest = max(longest, 1 + dfs(i, j + 1))
            memo[i][j] = longest
            return longest
        
        result = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result = max(result, dfs(i, j))
        return result