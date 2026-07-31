class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def backtrack(i, j, curr):
            if j >= len(s):
                result.append(curr.copy())
                return
            if i >= len(s):
                return
            
            if j == 0:
                if s[j : i+1] == s[i : : -1]:
                    curr.append(s[j : i+1])
                    backtrack(i+1, i+1, curr)
                    curr.pop()
            else:
                if s[j : i+1] == s[i : j-1 : -1]:
                    curr.append(s[j : i+1])
                    backtrack(i+1, i+1, curr)
                    curr.pop()
            backtrack(i+1, j, curr)
        
        backtrack(0, 0, [])
        return result
                    