class Solution:
    def getSum(self, a: int, b: int) -> int:
        result = 0
        carry = 0
        for i in range(32):
            bitA = (a >> i) & 1
            bitB = (b >> i) & 1
            bitSum = bitA ^ bitB ^ carry
            carry = (bitA + bitB + carry) >= 2
            if bitSum:
                result |= (1 << i)
        
        if result > 0x7FFFFFFF:
            result = ~(result ^ 0xFFFFFFFF)
        return result