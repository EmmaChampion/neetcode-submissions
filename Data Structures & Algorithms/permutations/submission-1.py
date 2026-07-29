class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.backtrack([], nums, [False] * len(nums))
        return self.result

    def backtrack(self, perm, nums, pick):
        if len(perm) == len(nums):
            self.result.append(perm.copy())
            return
        for i in range(len(nums)):
            if not pick[i]:
                pick[i] = True
                perm.append(nums[i])
                self.backtrack(perm, nums, pick)
                perm.pop()
                pick[i] = False