class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Find rotation
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle
        rotation = left

        #Binary search, factoring in rotation
        #left = rotation
        numsLen = len(nums)
        right = numsLen + rotation - 1
        while left <= right:
            middle = (left + right) // 2
            if target == nums[middle % numsLen]:
                return middle % numsLen
            elif target < nums[middle % numsLen]:
                right = middle - 1
            else:
                left = middle + 1
        return -1