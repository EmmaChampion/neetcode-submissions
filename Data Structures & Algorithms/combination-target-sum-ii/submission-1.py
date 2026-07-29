class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(i, subset, sumSoFar):
            if sumSoFar == target:
                result.append(subset.copy())
                return
            if sumSoFar > target or i >= len(candidates):
                return
            
            if sumSoFar + candidates[i] <= target:
                subset.append(candidates[i])
                backtrack(i + 1, subset, sumSoFar + candidates[i])
                subset.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            backtrack(i + 1, subset, sumSoFar)
            
        backtrack(0, [], 0)
        return result