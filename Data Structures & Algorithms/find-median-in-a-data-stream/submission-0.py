class MedianFinder:

    def __init__(self):
        #Max heap
        self.leftHalf = []
        #Min heap
        self.rightHalf = []

    def addNum(self, num: int) -> None:
        if not self.leftHalf and not self.rightHalf:
            heapq.heappush_max(self.leftHalf, num)
        elif num < self.leftHalf[0]:
            heapq.heappush_max(self.leftHalf, num)
        else:
            heapq.heappush(self.rightHalf, num)
        while len(self.leftHalf) - len(self.rightHalf) > 1:
            val = heapq.heappop_max(self.leftHalf)
            heapq.heappush(self.rightHalf, val)
        while len(self.rightHalf) - len(self.leftHalf) > 1:
            val = heapq.heappop(self.rightHalf)
            heapq.heappush_max(self.leftHalf, val)

    def findMedian(self) -> float:
        if len(self.leftHalf) > len(self.rightHalf):
            return self.leftHalf[0]
        elif len(self.rightHalf) > len(self.leftHalf):
            return self.rightHalf[0]
        else:
            left = self.leftHalf[0]
            right = self.rightHalf[0]
            return (left + right) / 2
        