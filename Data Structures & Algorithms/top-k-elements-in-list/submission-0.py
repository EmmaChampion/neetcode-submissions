class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1
        
        heap = []
        for num in frequencies.keys():
            heapq.heappush(heap, (frequencies[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        for i in range(k):
            val = heapq.heappop(heap)
            result.append(val[1])
        return result