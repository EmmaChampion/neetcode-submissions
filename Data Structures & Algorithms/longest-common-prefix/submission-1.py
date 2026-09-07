class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            prefixLen = 0
            for j in range(len(prefix)):
                if j >= len(strs[i]):
                    break
                if prefix[j] == strs[i][j]:
                    prefixLen += 1
                else:
                    break
            if prefixLen == 0:
                return ""
            if prefixLen < len(prefix):
                prefix = prefix[0:prefixLen]
        return prefix