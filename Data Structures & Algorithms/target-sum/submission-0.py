class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, goal):
            if i >= len(nums):
                if goal == 0:
                    return 1
                else:
                    return 0
            if (i, goal) in memo:
                return memo[(i, goal)]
            memo[(i, goal)] = dfs(i+1, goal - nums[i]) + dfs(i+1, goal + nums[i])
            return memo[(i, goal)]
        
        return dfs(0, target)