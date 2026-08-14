class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        prevMins = {}

        for coin in coins:
            if coin not in prevMins:
                prevMins[coin] = 1
        
        def dfs(amount):
            if amount == 0:
                return 0
            if amount in prevMins:
                return prevMins[amount]

            prev = math.inf
            for coin in coins:
                if amount - coin < 0:
                    continue
                attempt = dfs(amount - coin)
                if attempt < prev:
                    prev = attempt
            prevMins[amount] = 1 + prev
            return 1 + prev
        
        minCoins = dfs(amount)
        if math.isinf(minCoins):
            return -1
        return minCoins