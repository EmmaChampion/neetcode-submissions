class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1, 0, -1):
            nums[i - 1] = nums[i] ^ nums[i - 1]
        return nums[0]