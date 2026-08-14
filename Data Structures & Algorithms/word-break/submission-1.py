class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        splits = {}

        def dfs(i):
            if i == len(s):
                return True
            if i in splits:
                return splits[i]
            for j in range(i, len(s)):
                if s[i : j + 1] in words:
                    if dfs(j + 1):
                        splits[j + 1] = True
                        splits[i] = True
                        return True
                    else:
                        splits[j + 1] = False
            return False
        
        return dfs(0)