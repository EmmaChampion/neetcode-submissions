class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        possibilities = [-1] * len(s)

        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            if possibilities[i] != -1:
                return possibilities[i]
            valid = dfs(i+1)
            if i < len(s) - 1 and (s[i] == "1" or (s[i] == "2" and s[i+1] < "7")):
                valid += dfs(i+2)
            possibilities[i] = valid
            return valid
        
        return dfs(0)