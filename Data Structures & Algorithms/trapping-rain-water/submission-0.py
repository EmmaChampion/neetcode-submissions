class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0]
        max_right = [0] * len(height)
        for i in range(1, len(height) - 1):
            if height[i - 1] > max_left[i - 1]:
                max_left.append(height[i - 1])
            else:
                max_left.append(max_left[i - 1])
        for i in range(len(height) - 2, -1, -1):
            if height[i + 1] > max_right[i + 1]:
                max_right[i] = height[i + 1]
            else:
                max_right[i] = max_right[i + 1]
        
        total_volume = 0
        for i in range(len(height) - 1):
            volume_held = min(max_left[i], max_right[i]) - height[i]
            if volume_held > 0:
                total_volume += volume_held
        return total_volume