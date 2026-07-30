class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(curr, open, closed):
            if open > n:
                return
            if closed > open:
                return
            if len(curr) == 2 * n:
                result.append(curr)
                return
            
            backtrack(curr + "(", open + 1, closed)
            backtrack(curr + ")", open, closed + 1)
        
        backtrack("", 0, 0)
        return result