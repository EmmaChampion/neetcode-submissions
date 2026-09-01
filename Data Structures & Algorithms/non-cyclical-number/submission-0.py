class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            result = 0
            while n > 0:
                result += (n % 10) ** 2
                n //= 10
            if result in seen:
                return False
            seen.add(result)
            n = result
        return True