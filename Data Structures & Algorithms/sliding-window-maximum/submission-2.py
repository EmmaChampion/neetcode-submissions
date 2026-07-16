class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        left = 0
        right = 0
        while right < k:
            heapq.heappush_max(max_heap, nums[right])
            right += 1
        output = [max_heap[0]]

        while right < len(nums):
            left += 1
            if nums[left - 1] == max_heap[0]:
                heapq.heappop_max(max_heap)
                while max_heap and max_heap[0] not in nums[left:right]:
                    heapq.heappop_max(max_heap)
            heapq.heappush_max(max_heap, nums[right])
            output.append(max_heap[0])
            right += 1
        return output