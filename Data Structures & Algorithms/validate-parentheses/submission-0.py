class Solution:
    def isValid(self, s: str) -> bool:
        validPairs = {")":"(", "}":"{", "]":"["}
        stack = []
        for char in s:
            if char not in validPairs:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                compare = stack.pop()
                if validPairs[char] != compare:
                    return False
        if len(stack) != 0:
            return False
        else:
            return True