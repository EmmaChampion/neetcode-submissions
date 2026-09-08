class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        numVals = 0
        while i < len(nums):
            if nums[i] == val:
                numVals += 1
                nums.pop(i)
            else:
                i += 1
        return len(nums)