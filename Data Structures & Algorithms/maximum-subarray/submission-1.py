class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -math.inf
        curr = 0
        for num in nums:
            if curr < 0 and num > curr:
                curr = num
            else:
                curr += num
            if curr > maxSum:
                maxSum = curr
        
        return maxSum