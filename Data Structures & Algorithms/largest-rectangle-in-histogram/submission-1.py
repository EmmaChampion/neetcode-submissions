class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        numHeights = len(heights)
        nextSmaller = [-1] * numHeights
        stack = []
        for i in range(numHeights-1, -1, -1):
            while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if len(stack) > 0:
                nextSmaller[i] = stack[-1]
            stack.append(i)
        stack.clear()
        
        lastSmaller = [-1] * numHeights
        for i in range(numHeights):
            while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if len(stack) > 0:
                lastSmaller[i] = stack[-1]
            stack.append(i)
        
        maxRect = 0
        for i in range(numHeights):
            if lastSmaller[i] == -1:
                left = 0
            else:
                left = lastSmaller[i] + 1
            if nextSmaller[i] == -1:
                right = numHeights - 1
            else:
                right = nextSmaller[i] - 1
            rectHeight = heights[i]
            area = rectHeight * (right - left + 1)
            if area >maxRect:
                maxRect = area
        return maxRect