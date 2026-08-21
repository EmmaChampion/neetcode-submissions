class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dfs(i, j):
            print(i, j)
            if j >= len(p):
                if i >= len(s):
                    return True
                else:
                    return False
            
            if (i, j) in memo:
                return memo[(i, j)]
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j + 1 < len(p) and p[j + 1] == "*":
                if match:
                    memo[(i, j)] = dfs(i, j+2) or dfs(i+1, j)
                else:
                    memo[(i, j)] = dfs(i, j+2)
            else:
                if match:
                    memo[(i, j)] = dfs(i+1, j+1)
                else:
                    memo[(i, j)] = False
            return memo[(i, j)]
        
        return dfs(0, 0)
            