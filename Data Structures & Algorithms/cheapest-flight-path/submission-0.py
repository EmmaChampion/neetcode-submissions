class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [math.inf] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, price in flights:
                if math.isinf(prices[s]):
                    #Haven't reached source yet
                    continue
                tmpPrices[d] = min(tmpPrices[d], prices[s] + price)
            prices = tmpPrices
        
        if math.isinf(prices[dst]):
            return -1
        return prices[dst]