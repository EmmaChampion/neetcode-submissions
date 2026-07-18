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

        '''#Determine which half the number could be in
        if target == nums[0]:
            return 0
        elif target < nums[0] or rotation == 0:
            #Right half, after pivot
            left = rotation % len(nums)
            right = len(nums) - 1
        else:
            #Left half, before pivot
            left = 0
            right = rotation - 1
        
        #Binary search on the half the number could be in
        while left <= right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        return -1'''

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