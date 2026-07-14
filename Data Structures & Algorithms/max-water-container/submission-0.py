class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_volume = 0
        start = 0
        end = len(heights) - 1
        while start < end:
            left = heights[start]
            right = heights[end]
            current_volume = min(left, right) * (end - start)
            if current_volume > max_volume:
                max_volume = current_volume
            
            if left < right:
                start += 1
            else:
                end -= 1
        return max_volume
        