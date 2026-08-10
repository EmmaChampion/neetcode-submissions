class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #Cost to reach floor i
        cache = [-1] * len(cost)

        def dfs(i):
            if i == len(cost):
                return min(dfs(i-1), dfs(i-2))
            if i < 0:
                return 0
            if cache[i] == -1:
                cache[i] = min(dfs(i-1), dfs(i-2)) + cost[i]
            return cache[i]
        
        return dfs(len(cost))