# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, most, least):
            if not root:
                return True
            if root.val >= most or root.val <= least:
                return False
            leftValid = dfs(root.left, root.val, least)
            rightValid = dfs(root.right, most, root.val)
            return leftValid and rightValid
        
        return dfs(root, math.inf, -math.inf)