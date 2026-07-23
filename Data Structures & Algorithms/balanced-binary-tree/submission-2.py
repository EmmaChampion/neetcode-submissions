# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return [True, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            if not left[0] or not right[0]:
                return [False]
            if abs(left[1] - right[1]) > 1:
                return [False]
            else:
                return [True, (1 + max(left[1], right[1]))]
        
        result = dfs(root)
        return result[0]