class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        numsMinusFirst = nums[1:]
        numsMinusLast = nums[0:len(nums)-1]
        profitsMinusFirst = [-1] * (len(nums) - 1)
        profitsMinusLast = [-1] * (len(nums) - 1)

        def dfs(i, values, profits):
            if i < 0:
                return 0
            if i == len(values):
                return max(dfs(len(values) - 1, values, profits), dfs(len(values) -2, values, profits))
            if profits[i] == -1:
                profits[i] = max(dfs(i-2, values, profits), dfs(i-3, values, profits)) + values[i]
            return profits[i]
        
        maxMinusFirst = dfs(len(numsMinusFirst), numsMinusFirst, profitsMinusFirst)
        maxMinusLast = dfs(len(numsMinusLast), numsMinusLast, profitsMinusLast)
        return max(maxMinusFirst, maxMinusLast)