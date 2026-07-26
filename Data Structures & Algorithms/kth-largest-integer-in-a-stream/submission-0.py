class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.maxheap = nums
        for i in range(len(self.maxheap)):
            self.maxheap[i] *= -1
        heapq.heapify(self.maxheap)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.maxheap, -1 * val)
        kSmallest = heapq.nsmallest(self.k, self.maxheap)
        return kSmallest[-1] * -1