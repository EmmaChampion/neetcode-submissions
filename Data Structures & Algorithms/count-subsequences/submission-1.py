class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        memo = [[-1] * len(t) for i in range(len(s))]

        def dfs(i, j):
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            memo[i][j] = dfs(i+1, j)
            if s[i] == t[j]:
                memo[i][j] += dfs(i+1, j+1)
            return memo[i][j]
        
        return dfs(0, 0)