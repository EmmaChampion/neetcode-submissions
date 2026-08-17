class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Top row (0): canBuy = False
        #Bottom row (1): canBuy = True
        memo = [[-1] * len(prices) for i in range(2)]

        def dfs(i, canBuy):
            if i >= len(prices):
                return 0
            
            if canBuy:
                if memo[1][i] != -1:
                    return memo[1][i]
                memo[1][i] = max(dfs(i+1, True), dfs(i+1, False) - prices[i])
                return memo[1][i]
            else:
                if memo[0][i] != -1:
                    return memo[0][i]
                memo[0][i] = max(dfs(i+1, False), prices[i] + dfs(i+2, True))
                return memo[0][i]
        
        return dfs(0, True)