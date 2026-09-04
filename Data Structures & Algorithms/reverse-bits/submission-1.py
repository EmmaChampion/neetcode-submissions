class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            if (n >> i) & 1:
                result |= 1 << (31 - i)
        return result