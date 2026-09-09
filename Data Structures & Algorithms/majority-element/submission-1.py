class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
                if seen[num] >= len(nums)/2:
                    return num
            else:
                seen[num] = 1