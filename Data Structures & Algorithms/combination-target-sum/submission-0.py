class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(i, sumSoFar, target):
            if sumSoFar > target:
                return
            elif sumSoFar == target:
                result.append(subset.copy())
                return
            for j in range(i, len(nums)):
                num = nums[j]
                subset.append(num)
                backtrack(j, sumSoFar + num, target)
                subset.pop()
        
        backtrack(0, 0, target)
        return result
            