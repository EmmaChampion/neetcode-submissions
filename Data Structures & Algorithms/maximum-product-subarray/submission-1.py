class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        globalMax = nums[0]
        prevMax = nums[0]
        prevMin = nums[0]

        for i in range(1, len(nums)):
            temp = prevMax * nums[i]
            prevMax = max(temp, prevMin * nums[i], nums[i])
            prevMin = min(temp, prevMin * nums[i], nums[i])

            if prevMax > globalMax:
                globalMax = prevMax
        
        return globalMax