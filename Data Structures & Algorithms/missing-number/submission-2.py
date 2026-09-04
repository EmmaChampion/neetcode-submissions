class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            if nums[0] == 0:
                return 1
            else:
                return 0
        result = 0
        for num in nums:
            result = result ^ num
        nextBit = math.ceil(math.log(len(nums) + 1, 2))
        for i in range(len(nums) + 1, 2**nextBit):
            result = result ^ i
        return result