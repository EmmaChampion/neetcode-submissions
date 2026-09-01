class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        currDigit = 1
        digits[-1] += 1
        while currDigit < len(digits):
            if digits[len(digits) - currDigit] >= 10:
                digits[len(digits) - currDigit - 1] += 1
                digits[len(digits) - currDigit] %= 10
                currDigit += 1
            else:
                return digits
        if digits[0] >= 10:
            digits[0] %= 10
            return [1] + digits
        return digits