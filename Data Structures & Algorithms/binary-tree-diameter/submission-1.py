# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDia = 0

        def maxHeight(root):
            if root is None:
                return 0
            left = maxHeight(root.left)
            right = maxHeight(root.right)
            diameter = left + right
            nonlocal maxDia
            if diameter > maxDia:
                maxDia = diameter
            return 1 + max(left, right)
        
        maxHeight(root)
        return maxDia