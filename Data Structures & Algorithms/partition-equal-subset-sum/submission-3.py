class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        possible = [[-1] * (total//2 + 1) for i in range(len(nums))]
        
        def dfs(i, goal):
            if goal == 0:
                return True
            if i >= len(nums):
                return False
            if goal < 0:
                return False
            if possible[i][goal] != -1:
                return possible[i][goal]
            
            possible[i][goal] = dfs(i+1, goal) or dfs(i+1, goal-nums[i])
            return possible[i][goal]
        
        return dfs(0, total//2)