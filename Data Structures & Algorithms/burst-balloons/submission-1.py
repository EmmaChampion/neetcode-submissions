class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}

        def calc(left, right):
            if left > right:
                return 0
            if (left, right) in memo:
                return memo[(left, right)]

            best = 0
            for i in range(left, right+1):
                coins = (nums[i] * nums[left-1] * nums[right+1]) + calc(left, i-1) + calc(i+1, right)
                if coins > best:
                    best = coins
            memo[(left, right)] = best
            return memo[(left, right)]
        
        return calc(1, len(nums) - 2)