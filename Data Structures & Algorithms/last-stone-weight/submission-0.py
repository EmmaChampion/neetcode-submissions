class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop(stones) * -1
            stone2 = heapq.heappop(stones)* -1
            if stone1 == stone2:
                continue
            elif stone1 > stone2:
                stone1 -= stone2
                heapq.heappush(stones, stone1 * -1)
            else:
                stone2 -= stone1
                heapq.heappush(stones, stone2 * -1)
        
        if len(stones) == 0:
            return 0
        return stones[0] * -1