class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = 0
        for i in range(len(piles)):
            if piles[i] > right:
                right = piles[i]
        
        left = 1
        minPerHour = math.inf
        while left <= right:
            middle = (left + right) // 2
            timeTaken = 0
            for pileSize in piles:
                timePerPile = math.ceil(pileSize / middle)
                timeTaken += timePerPile
            if timeTaken > h:
                left = middle + 1
            else:
                if middle < minPerHour:
                    minPerHour = middle
                right = middle - 1
        return minPerHour

