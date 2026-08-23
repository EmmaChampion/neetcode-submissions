class Solution:
    def jump(self, nums: List[int]) -> int:
        left = 0
        right = 0
        steps = 0
        while right < len(nums) - 1:
            steps += 1
            farthest = 0
            for i in range(left, right + 1):
                if i + nums[i] > farthest:
                    farthest = i + nums[i]
            left = right + 1
            right = farthest
        
        return steps