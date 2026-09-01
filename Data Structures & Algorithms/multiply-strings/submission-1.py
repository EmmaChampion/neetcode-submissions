class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        stringNums = {"0": 0, "1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9}
        numStrings = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        val1 = 0
        for char in num1:
            val1 *= 10
            val1 += stringNums[char]
        val2 = 0
        for char in num2:
            val2 *= 10
            val2 += stringNums[char]
        
        product = val1 * val2

        result = []
        while product > 0:
            result.append(numStrings[product % 10])
            product //= 10
        return "".join(reversed(result))