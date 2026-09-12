import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return [nums[1], nums[0]]
            else:
                return nums
        items = random.sample(nums, 3)
        if (items[0] < items[1] and items[0] > items[2]) or (items[0] > items[1] and items[0] < items[2]):
            mid = items[0]
        elif (items[1] < items[0] and items[1] > items[2]) or (items[1] > items[0] and items[1] < items[2]):
            mid = items[1]
        else:
            mid = items[2]
        left = []
        right = []
        midCount = 0
        for num in nums:
            if num < mid:
                left.append(num)
            elif num > mid:
                right.append(num)
            else:
                midCount += 1
        return self.sortArray(left) + [mid] * midCount + self.sortArray(right)