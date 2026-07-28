class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        nums.sort()

        def backtrack(i, sumSoFar, target):
            if i >= len(nums) or sumSoFar > target:
                return
            elif sumSoFar == target:
                result.append(subset.copy())
                return
            for j in range(i, len(nums)):
                num = nums[j]
                if sumSoFar + num > target:
                    break
                subset.append(num)
                backtrack(j, sumSoFar + num, target)
                subset.pop()
        
        backtrack(0, 0, target)
        return result
            