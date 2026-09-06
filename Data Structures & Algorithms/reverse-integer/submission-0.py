class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        if negative:
            x = abs(x)
        result = 0
        while x > 0:
            result *= 10
            result += x % 10
            x //= 10
        if result > 2**31 - 1 or result < -2**31:
            return 0
        if negative:
            return -result
        return result