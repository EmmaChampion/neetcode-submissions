class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if len(stack) == 0:
                stack.append(i)
                continue
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                output[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        
        return output