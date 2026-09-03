class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            if n >> 1 != n / 2:
                count += 1
            n = n >> 1
        return count