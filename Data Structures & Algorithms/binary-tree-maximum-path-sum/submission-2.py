# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = -math.inf

        def dfs(root):
            nonlocal maxSum

            if not root:
                return 0
            maxLeft = dfs(root.left)
            maxRight = dfs(root.right)
            if root.val + maxLeft + maxRight > maxSum:
                maxSum = root.val + maxLeft + maxRight
            bestPath = root.val + max(maxLeft, maxRight)
            if bestPath < 0:
                return 0
            else:
                return bestPath
        
        dfs(root)
        return maxSum