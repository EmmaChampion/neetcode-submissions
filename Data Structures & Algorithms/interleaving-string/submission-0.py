class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        memo = [[-1] * (len(s2) + 1) for i in range(len(s1) + 1)]
        
        def dfs(i, j ,k):
            if k >= len(s3):
                return i == len(s1) and j == len(s2)
            if memo[i][j] != -1:
                return memo[i][j]

            if i < len(s1) and s1[i] == s3[k]:
                if dfs(i+1, j, k+1):
                    memo[i][j] = True
                    return True
            if j < len(s2) and s2[j] == s3[k]:
                if dfs(i, j+1, k+1):
                    memo[i][j] = True
                    return True
            memo[i][j] = False
            return False
        
        return dfs(0, 0, 0)