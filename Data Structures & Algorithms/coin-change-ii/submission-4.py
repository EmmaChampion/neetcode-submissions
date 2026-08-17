class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        combos = {}

        def dfs(i, goal):
            if (i, goal) in combos:
                return combos[(i, goal)]
            if goal < 0:
                return 0
            if goal == 0:
                return 1
            combos[(i, goal)] = 0
            for j in range(i, len(coins)):
                combos[(i, goal)] += dfs(j, goal - coins[j])
            return combos[(i, goal)]
        
        return dfs(0, amount)