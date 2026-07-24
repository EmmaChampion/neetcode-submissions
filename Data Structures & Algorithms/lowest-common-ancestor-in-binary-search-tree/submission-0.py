# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < q.val:
            lower = p.val
            higher = q.val
        else:
            lower = q.val
            higher = p.val
        curr = root
        while curr:
            if lower < curr.val and higher > curr.val:
                return curr
            if curr.val == lower or curr.val == higher:
                return curr
            if higher < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return None