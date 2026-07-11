class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed = []
        for num in range(len(nums)):
            if (target - nums[num]) not in needed:
                needed.append(nums[num])
            else:
                i = needed.index(target - nums[num])
                j = num
                return [i, j]
        return [0, 0]