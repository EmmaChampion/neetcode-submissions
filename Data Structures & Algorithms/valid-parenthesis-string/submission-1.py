class Solution:
    def checkValidString(self, s: str) -> bool:
        leftStack = []
        wildStack = []
        for i in range(len(s)):
            if s[i] == "(":
                leftStack.append(i)
            elif s[i] == "*":
                wildStack.append(i)
            else:
                #)
                if len(leftStack) > 0:
                    leftStack.pop()
                elif len(wildStack) > 0:
                    wildStack.pop()
                else:
                    return False
        while leftStack:
            if not wildStack:
                return False
            if leftStack.pop() > wildStack.pop():
                return False
        return True