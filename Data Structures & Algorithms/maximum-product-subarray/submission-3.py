class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        globalMax = nums[0]
        prevMax = 1
        prevMin = 1

        for num in nums:
            temp = prevMax * num
            prevMax = max(temp, prevMin * num, num)
            prevMin = min(temp, prevMin * num, num)

            if prevMax > globalMax:
                globalMax = prevMax
        
        return globalMax