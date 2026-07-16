class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            #Expression always valid - Don't need to check stack height
            if token == "+":
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(operand1 + operand2)
            elif token == "-":
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(operand1 - operand2)
            elif token == "*":
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(operand1 * operand2)
            elif token == "/":
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(int(operand1 / operand2))
            else:
                stack.append(int(token))
        
        return int(stack.pop())