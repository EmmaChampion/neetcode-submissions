class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[-1] * n for i in range(m)]
        paths[m - 1][n - 1] = 1

        def search(i, j):
            nonlocal m, n
            if i >= m:
                return 0
            if j >= n:
                return 0
            if paths[i][j] != -1:
                return paths[i][j]
            if i < m - 1 and j < n - 1:
                paths[i][j] = search(i+1, j) + search(i, j+1)
            else:
                #Along bottom and/or right edge
                paths[i][j] = 1
            return paths[i][j]
        
        return search(0, 0)