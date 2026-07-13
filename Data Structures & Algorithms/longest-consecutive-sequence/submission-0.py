class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxStreak = 0
        for num in numsSet:
            if num - 1 not in numsSet:
                streak = 1
                while num + streak in numsSet:
                    streak += 1
                if streak > maxStreak:
                    maxStreak = streak
        return maxStreak