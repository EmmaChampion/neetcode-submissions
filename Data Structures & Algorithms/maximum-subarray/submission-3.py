class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curr = 0
        for num in nums:
            if curr < 0:
                curr = num
            else:
                curr += num
            if curr > maxSum:
                maxSum = curr
        
        return maxSum