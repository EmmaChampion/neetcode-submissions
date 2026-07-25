# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        numGood = 0

        def dfs(root, maxPrev):
            nonlocal numGood
            if maxPrev <= root.val:
                numGood += 1
                maxPrev = root.val
            if root.left:
                dfs(root.left, maxPrev)
            if root.right:
                dfs(root.right, maxPrev)
        
        dfs(root, -1000)
        return numGood