class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        min_buy = prices[0]
        left = 0
        while left < len(prices) - 1 and prices[left] > prices[left + 1]:
            left += 1
            min_buy = prices[left]
        if left == len(prices) - 1:
            return 0
        
        right = left + 1
        max_profit = prices[right] - min_buy
        while right < len(prices):
            if prices[right] - min_buy > max_profit:
                max_profit = prices[right] - min_buy
            if prices[right] < min_buy:
                min_buy = prices[right]
            right += 1
        
        if max_profit < 0:
            return 0
        else:
            return max_profit








