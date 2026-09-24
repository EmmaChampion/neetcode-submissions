class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_counts = {}
        for num in nums:
            if num in num_counts:
                num_counts[num] += 1
            else:
                num_counts[num] = 1
        
        result = []
        n = len(nums)
        for num in num_counts:
            if num_counts[num] > math.floor(n/3):
                result.append(num)
        return result