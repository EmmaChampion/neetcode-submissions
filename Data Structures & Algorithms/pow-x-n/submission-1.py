class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        def power(base, exp):
            if exp == 0:
                return 1
            if exp == 1:
                return base
            if exp == 2:
                return base * base
            squared = power(base, exp // 2)
            return squared * squared * power(base, exp % 2)
        
        if n < 0:
            return 1 / power(x, abs(n))
        return power(x, n)