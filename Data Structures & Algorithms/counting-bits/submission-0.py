class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        for i in range(len(result)):
            num = i
            while num != 0:
                num = num & (num - 1)
                result[i] += 1
        return result