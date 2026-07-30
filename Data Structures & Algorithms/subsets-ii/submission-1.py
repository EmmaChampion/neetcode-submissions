class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()

        def backtrack(i, curr):
            if i >= len(nums):
                result.add(tuple(curr))
                return
            curr.append(nums[i])
            backtrack(i+1, curr)
            curr.pop()
            backtrack(i+1, curr)
        
        backtrack(0, [])
        return [list(item) for item in result]