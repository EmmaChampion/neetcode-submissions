class Solution:
    def rob(self, nums: List[int]) -> int:
        profits = [-1] * len(nums)

        def dfs(i):
            if i < 0:
                return 0
            if profits[i] == -1:
                profits[i] = max(dfs(i-2), dfs(i-3)) + nums[i]
            return profits[i]
        
        return max(dfs(len(nums) - 1), dfs(len(nums) - 2))